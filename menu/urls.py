from django.urls import path
from menu.views import *

app_name='menu'

urlpatterns = [
    path('', menu, name="menu"),
]