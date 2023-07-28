from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers= customers.count()
    total_orders=orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending =orders.filter(status='Pending').count()


    context = {'orders':orders,'customers':customers,'total_customers':total_customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}



    return render(request,'test_accounts/dashboard.html',{'context':context})

def about(request):
    return render(request,'test_accounts/about.html')

def products(request):
   products = Product.objects.all() # a query ..
   return render(request,'test_accounts/products.html',{'products':products})


def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders=orders.count()
    context ={'customer':customer,'orders':orders,'total_orders':total_orders}
    return render(request,'test_accounts/customers.html',{'context':context})
