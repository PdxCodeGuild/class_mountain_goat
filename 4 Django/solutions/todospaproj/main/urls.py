


from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.todos, name='todos'),
    path('priorities/', views.priorities, name='priorities'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('complete_todo/', views.complete_todo, name='complete_todo'),
    path('delete_todo/', views.delete_todo, name='delete_todo'),
    path('clear_completed/', views.clear_completed, name='clear_completed'),
    path('save_edited_todo/', views.save_edited_todo, name='save_edited_todo'),
]

