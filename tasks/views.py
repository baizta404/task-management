from django.shortcuts import render
from django.http import HttpResponse


def user_dashboard(request):
    return render(request,"dashboard/user-dashboard.html")

def manager_dashboard(request):
    return render(request,"dashboard/manager-dashboard.html")

def testt(request):
    context = {
        "names":["Mahmud","Ahamed","John"]
    }
    return render(request,'test.html',context)