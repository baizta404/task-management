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

#with the help of forms.Form in form.py
# def create_task(request):
#     employees =Employee.objects.all()
#     form = TaskForm(employees=employees)
#     if request.method == 'POST':
#         form = TaskForm(request.POST,employees=employees)
#         if form.is_valid():
#             data = form.cleaned_data
#             title = data.get('title')
#             description =data.get('description')
#             due_date = data.get('due_date')
#             assigned_to =data.get('assigned_to')

#             task= Task.objects.create(
#                 title=title,description=description,due_date=due_date
#                 )
            
#             #assign employee to tasks
#             for emp_id in assigned_to:
#                 employee = Employee.objects.get(id=emp_id)
#                 task.assigned_to.add(employee)
            
#             return HttpResponse('Task added Succesfully')
    
#     return render(request,'task-form.html',{'form':form})

"""For Model Form"""
def create_task(request):
    form = TaskModelForm()
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'task-form.html',{"form":form,'message':'Task added succesfully'})
    
    return render(request,'task-form.html',{'form':form})