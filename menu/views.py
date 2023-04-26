from django.shortcuts import render
from .models import *

# Create your views here.
def menu(request):
        menus = Menu.objects.all()
        return render(request, 'menu/menu_list.html', {'menus':menus})