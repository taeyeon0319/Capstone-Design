from django.urls import path
from main.views import *
from menu.views import *

app_name='main'

urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('call/', employee_call, name="employee_call"),
    path('cart/', cart_list, name="cart_list"),
]