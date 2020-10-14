from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.forms import modelformset_factory
from .models import *
from .forms import *
import datetime

# Create your views here.

def index(request):
    SendTec = SendRecord.objects.filter(done = False)
    returnedTec = SendRecord.objects.filter(done = True)
    tec = Technics.objects.all()
    dep = Department.objects.all()
    user = request.user
   
    context_dict = {'SRs':SendTec,'tecs':tec,'deps':dep,'rtec':returnedTec, 'user':user, 'url':request.path_info}
    return render(request,'pages/index.html',context = context_dict)

def technic(request):
    tec = Technics.objects.filter(writeoff = False)
    TForm = TecForm(request.POST)
    err = ''
    if TForm.is_valid():
        try:
            curr = get_object_or_404(Technics,serial = request.POST.get('serial'))
        except Http404:
            curr = None
        if curr == None:
            TForm.save(commit=True)
            return HttpResponseRedirect('')
        else:
            err = 'Техника с таким серийным номером уже существует'

        

    return render(request,'pages/technic.html', {'tecs':tec,'form':TForm,'err':err})

def del_tec(request,id):
    pass

def add_record(request):
    RcForm = RecForm(request.POST)
    tecid = request.POST.get('technics')
    err = ''

    if RcForm.is_valid():
        tec = get_object_or_404(Technics, pk = tecid)
        if tec.busy == False:
            tec.busy = True
            tec.save()
            rc = RcForm.save(commit=True)
            rc.get_date = datetime.date.today()
            rc.save()
            return redirect('/')

        else:
            err = 'Такой картридж уже отправлен'
            
    return render(request,'add_record.html',context = {'rcform':RcForm,'err':err,'url':request.path_info})

def add_dep(request):
    DepForm = DepartForm(request.POST)
    
    if DepForm.is_valid():
        DepForm.save(commit=True)
        
        return redirect('/')
    return render(request,'add_dep.html',context = {'depform':DepForm,'url':request.path_info})

def add_tec(request):
    TForm = TecForm(request.POST)
    if TForm.is_valid():
        TForm.save(commit=True)
        print(request.POST)
        return redirect('/')
    return render(request,'add_tec.html',context = {'tform':TForm,'url':request.path_info})

def edit_rec(request,id):
    rc = get_object_or_404(SendRecord,pk = id)
    if request.method == 'POST':
        RcForm = RecForm(request.POST,instance = rc)
        if RcForm.is_valid():
            rc = RcForm.save(commit = True)
            return redirect('/')
    else:
        RcForm = RecForm(instance = rc)
        

    context_dict = {'rcform':RcForm}
    return render(request,'add_record.html',context_dict)

    
def send_tec(request,id):
    sr = get_object_or_404(SendRecord,pk = id)
    now = datetime.date.today()
    sr.send_date = now
    sr.save()

    return redirect('/')

def confirm_tec(request,id):
    sr = get_object_or_404(SendRecord,pk = id)
    now = datetime.date.today()
    sr.retus_date = now
    sr.save()

    return redirect('/')

def writeoff(request,id):
    sr = get_object_or_404(SendRecord,pk = id)
    tec = get_object_or_404(Technics, pk = sr.technics.id)
    now = datetime.date.today()
    
    sr.retus_date = now
    tec.busy = False
    tec.writeoff = True
    sr.done = True
    
    sr.save()
    tec.save()

    return redirect('/')

def return_tec(request,id):
    sr = get_object_or_404(SendRecord,pk = id)
    tec = get_object_or_404(Technics, pk = sr.technics.id)
    
    now = datetime.date.today()
    sr.ret_date = now
    sr.done = True
    sr.save()
    tec.busy = False
    tec.save()

    return redirect('/')