from django.contrib import admin

from .models import TodoItem, Priority

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'price')
# admin.site.register(Book, BookAdmin)


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('priority', 'text', 'date_created', 'date_completed')
admin.site.register(TodoItem, TodoItemAdmin)


class PriorityAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')
admin.site.register(Priority, PriorityAdmin)

