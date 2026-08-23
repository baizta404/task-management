from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task,TaskDetail
from datetime import date

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
    pending_tasks = Task.objects.filter(status='PENDING')
    completed_tasks = Task.objects.filter(is_completed= True)
    today_due_dates = Task.objects.filter(due_date= date.today())
    priority_tasks = TaskDetail.objects.exclude(priority='H')

    return render(request,'show_task.html',{'priority_tasks':priority_tasks})