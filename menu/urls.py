from django.urls import path
from menu.views import *

app_name='menu'

urlpatterns = [
    path('', menu, name="menu"),
    path('cart_push', cart_push, name="cart_push"),
    path('delete', cart_delete, name="cart_delete"),
]