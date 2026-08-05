from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
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
    employees = Employee.objects.all()
    form = TaskForm(employees= employees)

    if request.method == 'POST':
        form = TaskForm(request.POST,employees=employees)
        if form.is_valid():
           data = form.cleaned_data
           title = data.get('title')
           description = data.get('description')
           due_date = data.get('due_date')
           assigned_to = data.get('assigned_to')
           task = Task.objects.create(title=title,description=description,due_date=due_date)
           #Assign employe to tasks
           for emp_id in assigned_to:
               employee = Employee.objects.get(id=emp_id)
               task.assigned_to.add(employee)

           return HttpResponse('Task Added Sucessfuly')
    print(Task.objects.all())
    context = {'form':form}
    return render(request,'./taskform.html',context)
#6.4 -> start korte hobe