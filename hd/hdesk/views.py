from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    SendTec = SendRecord.objects.filter(ret_date = None)
    tec = Technics.objects.all()
    dep = Department.objects.all()
   
    context_dict = {'SRs':SendTec,'tecs':tec,'deps':dep}
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
    rc = SendRecord.objects.filter(id = id)
    RcForm = RecForm(initial = {
        'technics': rc[0].technics,
        'depart': rc[0].depart,
        'send_date':rc[0].send_date,
        'ret_date':rc[0].ret_date,
        'repair_reason':rc[0].repair_reason
    })
    print(request.GET.get('id',1))

    context_dict = {'rcform':RcForm}
    return render(request,'add_record.html',context_dict)
