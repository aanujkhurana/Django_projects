from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('record/<int:pk>/', views.record, name='record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
    path('add_record', views.add_record, name='add_record'),
    path('edit_record/<int:pk>', views.edit_record, name='edit_record'),
]