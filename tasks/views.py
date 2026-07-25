from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Welcome to home')
def show_task(request):
    return HttpResponse('Oi cha testingg show task')
def show_specific_task(request,id):
    print(id)
    print('type of id', type(id))
    return HttpResponse(f'{id} showing specing task')