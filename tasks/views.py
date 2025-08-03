from django.shortcuts import render
from django.http import HttpResponse


def user_dashboard(request):
    return render(request,"userdashboard.html")