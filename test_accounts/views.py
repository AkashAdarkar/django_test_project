from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from  .forms  import OrderForm,CustomerForm



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


####CUSTOMERS###
def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders=orders.count()
    context ={'customer':customer,'orders':orders,'total_orders':total_orders}
    return render(request,'test_accounts/customers.html',{'context':context})


def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'test_accounts/customer_forms/create_user_form.html',{'context':context})



def updateCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form=CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context={'form':form}
    return render(request,'test_accounts/customer_forms/update_customer_form.html',{'context':context})


def deleteCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    
    context={'customer':customer}
    return render(request,'test_accounts/customer_forms/delete_user_form.html',{'context':context})



###ORDER####

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print('printing POST',request.POST)
        form =OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'test_accounts/order_forms/create_order_form.html',{'context':context})    




def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order) 
    if request.method == 'POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/') 
        

    context={'form':form}
    return render(request,'test_accounts/order_forms/update_order_form.html',{'context':context})


def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    # customer=Customer.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    
    context = {'order':order}
    return render(request,'test_accounts/order_forms/delete_order_form.html',{'context':context})
