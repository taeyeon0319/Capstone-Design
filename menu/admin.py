from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

admin.site.register(Menu, PostAdmin)
admin.site.register(Cart)
# Register your models here.
