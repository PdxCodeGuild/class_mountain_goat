from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItem
from django.utils import timezone


def index(request):
    todo_items = ToDoItem.objects.filter(completed_date__isnull=True).order_by('-created_date')
    completed_items = ToDoItem.objects.filter(completed_date__isnull=False).order_by('-created_date')
    context = {
        'todo_items': todo_items,
        'completed_items': completed_items,

    }
    return render(request, 'todoapp/index.html', context)

def save(request):
    todo_item_description = request.POST['todo_item_description']
    todo_item = ToDoItem(description=todo_item_description, completed_date=None)
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))

# by path
def complete(request, todo_item_id):
    # todo_item = ToDoItem.objects.get(id=todo_item_id)
    todo_item = get_object_or_404(ToDoItem, id=todo_item_id)
    todo_item.completed_date = timezone.now()
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))

# by query string
def complete2(request):
    # print(request.GET)
    # return HttpResponse('ok')
    todo_item_id = request.GET['todo_item_id']
    todo_item = get_object_or_404(ToDoItem, id=todo_item_id)
    todo_item.completed_date = timezone.now()
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))

# by form data
def complete3(request):
    # print(request.POST)
    # return HttpResponse('ok')
    todo_item_id = request.POST['todo_item_id']
    todo_item = get_object_or_404(ToDoItem, id=todo_item_id)
    todo_item.completed_date = timezone.now()
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))

def delete(request, todo_item_id):
    todo_item = get_object_or_404(ToDoItem, id=todo_item_id)
    todo_item.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))

