from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")
    
def blog(request):
    return render(request, "blog.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def teams(request):
    return render(request, "teams.html")

def google(request):
    return redirect("https://google.com")


