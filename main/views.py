from django.shortcuts import render

# Create your views here.
def mainpage(request):
        return render(request, 'main/mainpage.html')

def employee_call(request):
        return render(request, 'main/employee_call.html')

def pay(request):
        return render(request, 'main/pay.html')

def final(request):
        return render(request, 'main/final.html')