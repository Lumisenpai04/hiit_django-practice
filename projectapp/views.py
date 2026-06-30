from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")
    


def about(request):
    return HttpResponse("My About page!!!")

def google(request):
    return redirect("https://google.com")


