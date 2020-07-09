from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import json
import datetime
# Create your views here.

def home(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'web/index.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
    context={'items':items,'order':order}
    return render(request,'web/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
    context={'items':items,'order':order}
    return render(request,'web/checkout.html',context)


def UpdateItem(request):
    data=json.loads(request.body)
    productID=data['productID']
    action=data['action']
    print('productID = ',productID)
    print('action = ',action)

    customer=request.user.customer
    product=Product.objects.get(id=productID)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)
    print(type(order))
    print(type(orderItem))
    print(type(product))
    if orderItem.quantity<=0:
        orderItem.delete()
# 
    if action=='add':
        orderItem.quantity=(orderItem.quantity + 1 )
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    # orderItem.save()

    return JsonResponse('Item was added',safe=False)


def ProcessOrder(request):
    # print('data',request.body)
    transaction_ID=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        total=float(data['form']['total'])
        order.transaction_id=transaction_ID
    if total==order.get_cart_total:
        order.complete=True
    order.save()

    if order.shipping==True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zip_code=data['shipping']['zip']
        )

    return JsonResponse('Order Processed',safe=False)