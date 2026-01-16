from django.contrib import admin

from .models import Thing, Category

# Register your models here.
admin.site.register(Thing)
admin.site.register(Category)