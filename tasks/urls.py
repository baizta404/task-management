from django.urls import path
from tasks.views import manager_dashboard, user_dashboard,testt,create_task

urlpatterns=[
    path('manager-dashboard/',manager_dashboard),
    path('user-dashboard/',user_dashboard),
    path('test/',testt),
    path('create-task/',create_task)
]