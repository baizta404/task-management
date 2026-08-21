from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task

# Create your views here.
def manager_dashboard(request):
    return render(request,'./dashboard/manager_dashboard.html')

def user_dashboard(request):
    return render(request,'./dashboard/user_dashboard.html')

def test(requset):
    context = {
        'names':['Mahmud','Rahim','Rana','Mohsin','John','Iktiup','Zakir','Rohan']
    }
    return render(requset,'./test.html',context)

def create_task(request):
    form = TaskModelForm()

    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'./taskform.html',{'form':form,'message':'task added succesfully'})
            
    context = {'form':form}
    return render(request,'./taskform.html',context)

def view_task(request):
    #retrive all data from tasks.model
    tasks = Task.objects.all()
    task_3 = Task.objects.get(id=1)
    return render(request,'show_task.html',{'tasks':tasks,'task3':task_3})