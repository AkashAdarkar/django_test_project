from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'test_accounts/dashboard.html')

def about(request):
    return render(request,'test_accounts/about.html')

def products(request):
   return render(request,'test_accounts/products.html')


def customers(request):
    return render(request,'test_accounts/customers.html')
