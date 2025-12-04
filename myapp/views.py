from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    # return HttpResponse("this is about view")
    return render(request,"about.html")
def home(request):
    return render(request,"home.html")
def contact(request):
    return render(request,"contact.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")