from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import datetime
from django.contrib import auth
from .models import *
import json
# Create your views here.

@login_required(login_url='sign')
def products(request):
    productItems= Product.objects.filter(active=True)
    customer=request.user
    order,created=Order.objects.get_or_create(user=customer,complete=False)
    items=order.orderitem_set.all()
    cartItems=order.get_cart_items

    context={'products':productItems,'cartItems':cartItems}
    return render(request,'product/products.html',context)


def logout(request):
    auth.logout(request)
    return redirect('sign')

def cart(request):
    customer=request.user
    order,created=Order.objects.get_or_create(user=customer,complete=False)
    items=order.orderitem_set.all()
    context={'items':items,'order':order}
    return render(request,'product/cart.html',context)

def checkOut(request):
    customer=request.user
    order,created=Order.objects.get_or_create(user=customer,complete=False)
    items=order.orderitem_set.all()
    cartItems=order.get_cart_items
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'product/checkout.html',context)

def updateItem(request):

    data=json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
	    orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
	    orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
	    orderItem.delete()
    cartItems=order.get_cart_items
    cartTotal=order.get_cart_total
    items=order.orderitem_set.all()
    itemquantity=orderItem.quantity
    
    return JsonResponse({"cartItems":cartItems,"itemQuantity":itemquantity,"cartTotal":cartTotal},safe=False)


def processOrder(request):
    data=json.loads(request.body)
    transaction_id=datetime.datetime.now().timestamp()
    customer=request.user
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    print(data['total'])
    total=float(data['total'])

    print(total)
    order.transaction_id=transaction_id

    #checking the carttotal with backend to avoid manipulation 

    if total== order.get_cart_total:
        order.complete=True
    order.save()

    ShippingAddress.objects.create(
        user=customer,
        order=order,
        address=data["shipping"]["address"],
        city=data["shipping"]["city"],
        zipcode=data["shipping"]["zipcode"],
        phoneNumber=data["shipping"]["phoneNumber"],
        )
        
    return JsonResponse("payment complete",safe=False)