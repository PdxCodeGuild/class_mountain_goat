from django.contrib import admin

from .models import Question, Choice, Contact, City

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Contact)
admin.site.register(City)
