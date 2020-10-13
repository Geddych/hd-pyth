from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
import datetime

# Create your views here.
def index(request):
    SendTec = SendRecord.objects.filter(ret_date = None)
    tec = Technics.objects.all()
    dep = Department.objects.all()
    woff = WriteOffTec.objects.all()
   
    context_dict = {'SRs':SendTec,'tecs':tec,'deps':dep,'woff':woff}
    return render(request,'index.html',context = context_dict)

def add_record(request):
    RcForm = RecForm(request.POST)

    if RcForm.is_valid():
        RcForm.save(commit=True)
        return redirect('/')
    return render(request,'add_record.html',context = {'rcform':RecForm})

def add_dep(request):
    DepForm = DepartForm(request.POST)
    
    if DepForm.is_valid():
        DepForm.save(commit=True)
        return redirect('/')
    return render(request,'add_dep.html',context = {'depform':DepForm})

def add_tec(request):
    TForm = TecForm(request.POST)
    if TForm.is_valid():
        TForm.save(commit=True)
        return redirect('/')
    return render(request,'add_tec.html',context = {'tform':TForm})

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

def write_off(request,id):
    sr = get_object_or_404(SendRecord,pk = id)
    
    name = sr.technics.name
    depart = sr.depart.name

    now = datetime.date.today()
    print(name,depart,now)
    wot = WriteOffTec(name = name, depart = depart,date_woff = now)
    sr.ret_date = now
    sr.save()
    wot.save()
    
    return redirect('/')
    
