from django.shortcuts import render
from django.http import HttpResponse

from .models import TodoItem

def index(request):
    todo_items = TodoItem.objects.all()
    context = {
        'title': 'Todo List',
        'todo_items': todo_items
    }
    return render(request, 'todoapp/index.html', context)

def about(request):
    return HttpResponse('about')

def blog(request):
    return HttpResponse('blog')

