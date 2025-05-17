from django.urls import path
from . import views

urlpatterns = [
    path('text', views.text, name='text'),
    path('list', views.list, name='list'),
    path('home', views.home, name="home"),
    path('todo', views.todo, name="todo"),
    
]
