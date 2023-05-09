from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def menu(request):
        menus_1 = Menu.objects.filter(category="오넛지")
        menus_2 = Menu.objects.filter(category="카츠")
        menus_3 = Menu.objects.filter(category="더푸리")
        menus_4 = Menu.objects.filter(category="카페")
        carts = Cart.objects.all()
        return render(request, 'menu/menu_list.html', 
                      {'menus_1':menus_1, 
                       'menus_2':menus_2, 
                       'menus_3':menus_3, 
                       'menus_4':menus_4,
                       'carts':carts})

def cart_push(request):
        new_cart =Cart()
        new_cart.name = request.POST.get("name")
        new_cart.price = request.POST.get("price")
        new_cart.save()

        return redirect('menu:menu')

def cart_delete(request):
        delete_cart = Cart.objects.all()
        delete_cart.delete()
        return redirect('main:mainpage')

def cart_list(request):
        carts = Cart.objects.all()
        return render(request, 'menu/cart_list.html', {'carts':carts})

def cart_delete_each(request, id):
        delete_cart_each = Cart.objects.get(id=id)
        delete_cart_each.delete()
        return redirect('menu:menu')

def cart_delete_each2(request, id):
        delete_cart_each = Cart.objects.get(id=id)
        delete_cart_each.delete()
        return redirect('main:cart_list')