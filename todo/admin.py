from django.contrib import admin

# Register your models here.
from .models import DateTime,ListToDo

admin.site.register(DateTime)
admin.site.register(ListToDo)