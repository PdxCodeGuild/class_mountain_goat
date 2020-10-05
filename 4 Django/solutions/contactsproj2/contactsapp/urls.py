

from django.urls import path
from . import views

app_name = 'contactsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('edit/<int:contact_id>/', views.edit, name='edit'),
]

