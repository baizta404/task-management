from django.urls import path
from tasks.views import user_dashboard

urlpatterns=[
    path('user-dashboard/',user_dashboard)
]