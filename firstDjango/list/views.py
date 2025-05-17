from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def list(request):
    return HttpResponse("THIS IS LIST PAGE")

def text(request):
    return HttpResponse("hello")

def home(request):
    return render(request, 'home.html')

def todo(request):
    items = TodoItem.objects.all()
    return render(request, 'todo.html', {'items': items})