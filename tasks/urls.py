from django.urls import path
from tasks.views import show_task,show_sepecific_task

urlpatterns=[
    path('show-task/',show_task)
    path('show-task/<int:id>',show_sepecific_task)
]