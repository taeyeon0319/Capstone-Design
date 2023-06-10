from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

tapNumber = 0


def menu(request):
    menus_1 = Menu.objects.filter(category="오넛지")
    menus_2 = Menu.objects.filter(category="카츠")
    menus_3 = Menu.objects.filter(category="더푸리")
    carts = Cart.objects.all()
    return render(request, 'menu/menu_list.html',
                  {'menus_1': menus_1,
                   'menus_2': menus_2,
                   'menus_3': menus_3,
                   'carts': carts,
                   'tapNumber': tapNumber})


def cart_push(request):
    global tapNumber

    cart_count = Cart.objects.count()
    if cart_count >= 6:
        messages.error(request, "Cart 모델 개수가 6개를 초과했습니다.")
        return redirect('menu:menu')

    new_cart = Cart()
    new_cart.name = request.POST.get("name")
    new_cart.price = request.POST.get("price")
    new_cart.image = request.POST.get("image_url")
    tapNumber = request.POST.get("tapNumber")
    new_cart.save()

    return redirect('menu:menu')


def cart_delete(request):
    delete_cart = Cart.objects.all()
    delete_cart.delete()
    return redirect('main:mainpage')


def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'menu/cart_list.html', {'carts': carts})


def cart_delete_each(request, id):
    delete_cart_each = Cart.objects.get(id=id)
    delete_cart_each.delete()
    return redirect('menu:menu')


def cart_delete_each2(request, id):
    delete_cart_each = Cart.objects.get(id=id)
    delete_cart_each.delete()
    return redirect('main:cart_list')
