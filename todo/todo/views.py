from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,"todo/home.html")

def task(request):
    return render(request,"todo/task.html")