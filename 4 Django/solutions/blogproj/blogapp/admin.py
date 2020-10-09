from django.contrib import admin
from django.contrib.auth.models import Group
from .models import BlogPost, Comment


admin.site.unregister(Group)

admin.site.register(BlogPost)
admin.site.register(Comment)

