from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.utils import timezone

from .models import TodoItem, Priority


def index(request):
    return render(request, 'main/index.html')


def add_todo(request):
    data = json.loads(request.body)
    
    # priority = Priority.objects.get(id=data['priority_id'])
    # todo_item = TodoItem(..., priority=priority)

    todo_item = TodoItem(text=data['todo_text'], priority_id=data['priority_id'])
    todo_item.save()

    return HttpResponse('ok')


def complete_todo(request):
    todo_item_id = request.GET['todo_item_id']
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.date_completed = timezone.now()
    todo_item.save()
    return HttpResponse('ok')

def delete_todo(request):
    todo_item_id = request.GET['todo_item_id']
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.delete()
    return HttpResponse('ok')


def todos(request):
    todos = TodoItem.objects.order_by('date_completed', '-priority', 'date_created')
    todo_data = []
    for todo in todos:
        todo_data.append({
            'id': todo.id,
            'text': todo.text,
            'priority': todo.priority.name,
            'date_created': todo.date_created.strftime('%Y-%m-%d %H:%M'),
            'date_completed': todo.date_completed.strftime('%Y-%m-%d %H:%M') if todo.date_completed else None,
        })
    return JsonResponse({'todos': todo_data})


def priorities(request):
    data = {'priorities': []}
    priorities = Priority.objects.all()
    for priority in priorities:
        data['priorities'].append({
            'id': priority.id,
            'name': priority.name,
            'order': priority.order,
        })
    return JsonResponse(data)


def clear_completed(request):
    completed_todos = TodoItem.objects.filter(date_completed__isnull=False)
    completed_todos.delete()

    return HttpResponse('ok')
