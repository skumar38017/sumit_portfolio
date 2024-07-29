"""
URL configuration for protfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Ensure the URL pattern is correct

    #----------------------------- Projects ---------------------------------------
    #       page name                   function name               function name
    path('two_tier_deployment', views.two_tier_deployment, name='two_tier_deployment'),  # Correct URL pattern and view
    path('3_tier_deployment', views.three_tier_deployment, name='three_tier_deployment'),  # Correct URL pattern and view
    path('AWS_DevOps_Demo_project_Deployment', views.AWS_DevOps_Demo_project_Deployment, name='AWS_DevOps_Demo_project_Deployment'), 
    path('End_to_End_Deployment', views.End_to_End_Deployment, name='End_to_End_Deployment'), 
    path('Hospital_Management', views.Hospital_Management, name='Hospital_Management'), 
    path('todo_application', views.Todo_Application, name='Todo_Application'), 
    path('ToDo_Web_app', views.ToDo_Web_app, name='ToDo_Web_app'), 
    path('user_management_system', views.User_Management_System, name='User_Management_System'), 
]



