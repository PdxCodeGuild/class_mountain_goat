from django.contrib import admin

from .models import TodoItem, Priority



class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_date')
admin.site.register(TodoItem, TodoItemAdmin)

admin.site.register(Priority)