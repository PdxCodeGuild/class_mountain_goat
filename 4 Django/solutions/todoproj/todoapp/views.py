from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import random
from django.utils import timezone
from .models import TodoItem

def index(request):
    todo_items = TodoItem.objects.all()
    context = {
        'todo_items': todo_items
    }
    return render(request, 'todoapp/index.html', context)


def savetodo(request):
    print(request.POST)
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, date_created=timezone.now())
    todo_item.save()
    return HttpResponseRedirect('/')


def about(request):
    context = {
        'message': 'hello world!',
        'temperature': random.randint(40, 100),
        'fruits': ['apples', 'bananas', 'pears'],
    }
    return render(request, 'todoapp/about.html', context)


def blogview(request):
    return HttpResponse('blog')


def redirect(request):
    return HttpResponseRedirect('https://google.com/')

def fruits(request):
    fruits = ['apples', 'bananas', 'pears']
    return JsonResponse({'fruits': fruits, 'num_results': 3})