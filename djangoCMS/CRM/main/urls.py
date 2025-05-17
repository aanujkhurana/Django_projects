from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
]
