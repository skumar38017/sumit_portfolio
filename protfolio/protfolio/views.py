from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.conf import settings

curl = settings.CURRENT_URL 



def index(request):
    return render(request, 'index.html')


# ------------------- projects-------------------------
def two_tier_deployment(request):
    return render(request, 'projects/two_tier_deployment.html')

def three_tier_deployment(request):
    return render(request, 'projects/3_tier_deployment.html')

def AWS_DevOps_Demo_project_Deployment(request):
    return render(request, 'projects/AWS_DevOps_Demo_project_Deployment.html')

def End_to_End_Deployment(request):
    return render(request, 'projects/End_to_End_Deployment.html')

def Hospital_Management(request):
    return render(request, 'projects/Hospital_Management.html')

def Todo_Application(request):
    return render(request, 'projects/todo_application.html')

def ToDo_Web_app(request):
    return render(request, 'projects/ToDo_Web_app.html')

def User_Management_System(request):
    return render(request, 'projects/user_management_system.html')
