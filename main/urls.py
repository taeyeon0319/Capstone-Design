from django.urls import path
from main.views import *

app_name='main'

urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('call/', employee_call, name="employee_call"),
]