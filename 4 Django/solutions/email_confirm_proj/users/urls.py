

from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('confirm/', views.confirm, name='confirm'),
    path('home/', views.home, name='home'),
]

