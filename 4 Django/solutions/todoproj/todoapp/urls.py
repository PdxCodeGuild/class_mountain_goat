from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns= [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    # by path
    path('complete/<int:todo_item_id>/', views.complete, name='complete'),
    # by query string
    path('complete2/', views.complete2, name='complete2'),
    # by form data
    path('complete3/', views.complete3, name='complete3'),
    path('delete/<int:todo_item_id>/', views.delete, name='delete'),

]