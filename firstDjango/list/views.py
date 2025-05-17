from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list(request):
    return HttpResponse("THIS IS LIST PAGE")

def text(request):
    return HttpResponse("hello")

def home(request):
    return render(request, 'home.html')

