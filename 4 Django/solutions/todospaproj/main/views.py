from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import TodoItem, Priority
import json





def index(request):
    priorities = Priority.objects.order_by('order')
    context = {
        'priorities': priorities
    }
    return render(request, 'main/index.html', context)


def todo(request):

    todos = TodoItem.objects.order_by('date_completed', '-priority__order', 'date_created')
    data = {'todos': []}

    for todo in todos:
        data['todos'].append({
            'text': todo.text,
            'priority': todo.priority.name,
            'date_created': todo.date_created.strftime('%Y-%m-%d'),
            'date_completed': todo.date_completed.strftime('%Y-%m-%d') if todo.date_completed else None,
        })

    return JsonResponse(data)

    # return JsonResponse({'apples': 1, 'bananas': 2})

def save_todo(request):
    data = json.loads(request.body)
    todo_item = TodoItem(text=data['todo_text'], priority_id=data['priority_id'])
    todo_item.save()
    return HttpResponse('ok')
