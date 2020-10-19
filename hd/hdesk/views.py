from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import Http404,HttpResponseRedirect,HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login

import datetime
import random

from .forms import *
from .resources import *




# Create your views here.

def index(request):
    err=''
    AuthForm = UserForm(request.POST)
    if request.method == "POST":
        user = authenticate(username = request.POST.get('username'),password = request.POST.get('password'))
        if user:
           login(request,user)
           return redirect('/records')
        else:
            err = 'Неправильные данные'


    return render(request,'pages/index.html',context = {'err':err,'form':AuthForm})

@login_required
def technic(request):
    def getExTec(s):
        try:
            tec = get_object_or_404(Technics,serial = s)
        except Http404:
            tec = None
        return tec
    tec = Technics.objects.filter(writeoff = False)
    TForm = TecForm(request.POST)
    err = ''
    
    if TForm.is_valid():
        
        tf = TForm.save(commit=True)
        serial = random.randint(100000,999999)
        exTec = getExTec(serial)
        while exTec != None:
            exTec = getExTec(serial)
        tf.serial = serial
        tf.save()
        return redirect('/technic')
    return render(request,'pages/technic.html', {'tecs':tec,'form':TForm,'err':err})

@login_required
def depart(request):
    deps = Department.objects.all()
    tec = Technics.objects.all()
    DForm = DepartForm(request.POST)
    if request.method == "POST":
        if DForm.is_valid:
            DForm.save(commit=True)   
            return redirect('/departments')


    return render(request,'pages/depart.html',context={'departs':deps,'form':DForm,'tec':tec})

@login_required
def del_tec(request,id):
    Technics.objects.filter(id = id).delete()
    return redirect('/technic')

@login_required
def edit_tec(request,id):
    tec = get_object_or_404(Technics,pk = id)
    TForm = TecForm(instance = tec)
    tecs = Technics.objects.filter(writeoff = False)
    if request.method == "POST":
        pass
    return render(request,'pages/technic.html',context = {'tform':TForm,'tecs':tecs})

@login_required
def records(request):
    sr = SendRecord.objects.filter(done = False)

    return render(request,'pages/records.html',context={'sr':sr})

@login_required
def add_record(request):
    sr = Technics.objects.filter(busy=False).filter(writeoff = False)
    RcForm = RecForm(request.POST)
    RcForm.fields['technics'].queryset = sr
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
            if rc.repair_reason == None:
                rc.repair_reason = 'Заправка'
            rc.save()
            return redirect('/records')
            
    return render(request,'actions/add_record.html',context = {'rcform':RcForm,'err':err,'url':request.path_info,'sr':sr})

@login_required
def add_tec(request):
    TForm = TecForm(request.POST)
    if TForm.is_valid():
        TForm.save(commit=True)
        print(request.POST)
        return redirect('/')
    return render(request,'add_tec.html',context = {'tform':TForm,'url':request.path_info})

@login_required
def edit_rec(request,id):
    rc = get_object_or_404(SendRecord,pk = id)
    if request.method == 'POST':
        RcForm = RecForm(request.POST,instance = rc)
        if RcForm.is_valid():
            rc = RcForm.save(commit = True)
            return redirect('/records')
    else:
        RcForm = RecForm(instance = rc)
        

    context_dict = {'rcform':RcForm}
    return render(request,'actions/add_record.html',context_dict)
  
@login_required  
def send_tec(request,id):
    sr = get_object_or_404(SendRecord,pk = id)
    now = datetime.date.today()
    sr.send_date = now
    sr.save()

    return redirect('/records')

@login_required
def confirm_tec(request,id):
    sr = get_object_or_404(SendRecord,pk = id)
    now = datetime.date.today()
    sr.retus_date = now
    sr.save()

    return redirect('/records')

@login_required
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

    return redirect('/records')

@login_required
def return_tec(request,id):
    sr = get_object_or_404(SendRecord,pk = id)
    tec = get_object_or_404(Technics, pk = sr.technics.id)
    
    now = datetime.date.today()
    sr.ret_date = now
    sr.done = True
    sr.save()
    tec.busy = False
    tec.save()

    return redirect('/records')

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def download_all_tec(request):
    queryset = Technics.objects.filter(writeoff=False)
    dataset = TecResource().export(queryset)

    response = HttpResponse(
            content_type='application/ms-excel',
        )
    response['Content-Disposition'] = 'attachment;filename = "technics from {}.xls"'.format(datetime.date.today())
    response.write(dataset.xls)
    return response

@login_required
def dowload_writeoff_tec(request):
    queryset = Technics.objects.filter(writeoff= True)
    dataset = TecResource().export(queryset)
    response = HttpResponse(
            content_type='application/ms-excel',
        )
    response['Content-Disposition'] = 'attachment;filename = "Writeoff from {}.xls"'.format(datetime.date.today())
    response.write(dataset.xls)
    return response

@login_required
def download_on_repair(request):
    queryset = SendRecord.objects.filter(done = False)
    dataset = SRResource().export(queryset)
    response = HttpResponse(
            content_type='application/ms-excel',
        )
    response['Content-Disposition'] = 'attachment;filename = "Sended from {}.xls"'.format(datetime.date.today())
    response.write(dataset.xls)
    return response