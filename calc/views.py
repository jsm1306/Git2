from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    return render(request,'dashboard.html',{'customers':customers,'orders':orders})

def products(request):
    products=Product.objects.all()
    return render(request,'products.html',{'products':products})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=val1+val2
    return render(request,'result.html',{'result':val3})
def customer(request, pk_test):
    customer=Customer.objects.get(id=pk_test)
    customers=Customer.objects.all()
    orders=customer.order_set.all()
    order_count=orders.count()
    context={'customers':customers, 'cust':customer,'orders':orders,'ordcount':order_count}
    return render(request,'customer.html',context)

from .forms import OrderForm
def createOrder(request):
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'order_form.html',context)

def updateOrder(request, pk):

    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
        form=OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'order_form.html',context)

def deleteOrder(request, pk): 
    order=Order.objects.get(id=pk) 
    if request.method=="POST": 
        order.delete() 
        return redirect('/') 
    context={'item':order}
    return render(request,'delete.html',context) 

from django.contrib.auth.forms import UserCreationForm 
def registerPage(request): 
    form=UserCreationForm() 
    if request.method=="POST": 
        form=UserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('login') 
        else: 
            messages.success(request,"Password does not follow the rules") 
            
    context={'form':form} 
    return render(request, 'register.html', context)