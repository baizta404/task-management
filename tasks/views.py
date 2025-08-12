from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task


def user_dashboard(request):
    return render(request,"dashboard/user-dashboard.html")

def manager_dashboard(request):
    return render(request,"dashboard/manager-dashboard.html")

def testt(request):
    context = {
        "names":["Mahmud","Ahamed","John"]
    }
    return render(request,'test.html',context)

def create_task(request):
    # employees = Employee.objects.all()

    form = TaskModelForm() #for GET by default #employees=employees

    if request.method =='POST':
        form = TaskModelForm(request.POST)

        if form.is_valid():
            """But for Model Form its not needed to have clean data"""
            form.save()
            return render(request,'task-form.html',{'form':form,'message':'task added succesfully'})

            """For Django form its needed to clean the data"""
            # data = form.cleaned_data
            # title = data.get("title")
            # description = data.get("description")
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to') #list = [1,3]
            # task = Task.objects.create(title=title,description=description,
            #                            due_date=due_date)
            # # Assign employee to task
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employee)

            return HttpResponse("Task Added Succesfully")

    context={'form':form}
    return render(request,'task-form.html',context)