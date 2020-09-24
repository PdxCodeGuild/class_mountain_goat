
from django.urls import path
from . import views


app_name = 'contactsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:contact_id>/', views.details, name='details'),
    path('<int:contact_id>/delete', views.delete, name='delete')
]


