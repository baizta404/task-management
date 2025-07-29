from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the task management system")

def contact(request):
    return HttpResponse("<h1 style='color:red;text-align:center'>Number Diya Ki Korba</h1>")

def show_task(request):
    return HttpResponse("this is our task page.....")

def show_sepecific_task(request,id):
    print("id",id)
    print("id type",type(id))
    return HttpResponse(f"This is a sepecific task page {id}")