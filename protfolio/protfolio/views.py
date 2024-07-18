from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.conf import settings

curl = settings.CURRENT_URL 



def index(request):
    return render(request, 'index.html')
