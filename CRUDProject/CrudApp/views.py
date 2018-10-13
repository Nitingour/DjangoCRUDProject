from django.shortcuts import render
from CrudApp.forms import *
# Create your views here.
def empview(request):
    if request.method=='GET':
        print('GET Invoked......')
        empform=EmployeeForm()
        return render(request,'CrudApp/addemp.html',{'eform':empform})
    if request.method=='POST':
        print('POST Invoked......')
        empform=EmployeeForm(request.POST)
        if empform.is_valid():
            empform.save()
            return render(request,'CrudApp/msg.html',{'msg':'Registration Success...'})
 #employees=Employee.objects.all().filter(ename__iexact='Amit').order_by('-id')
def homeview(request):
    employees=Employee.objects.all()
    return render(request,'CrudApp/home.html',{'employees':employees})

def deleteempview(request,pid):
    emp=Employee.objects.get(id=pid)
    emp.delete()
    return render(request,'CrudApp/msg.html',{'msg':'Deleted Successfully...'})

def updateempview(request,pid):
    emp=Employee.objects.get(id=pid)
    if request.method=='GET':
        return render(request,'CrudApp/update.html',{'emp':emp})
    if request.method=='POST':
        empform=EmployeeForm(request.POST,instance=emp)
        if empform.is_valid():
            empform.save()
            return render(request,'CrudApp/msg.html',{'msg':'Updated Successfully...'})
