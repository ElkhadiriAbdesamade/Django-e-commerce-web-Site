from django.shortcuts import render, redirect
from django.http import JsonResponse
from store.models import *
import json
import datetime
from store.utils import cookieCart, cartData,guestOrder
from .login import Login


def store(request):
    customor = request.session.get('customer')

    if not customor:
        request.session["customer"]=''

    data = cartData(request)

    cartItems = data['cartItems']
    favorites = Favorite.objects.all()
    products = Product.objects.all()

    context = {'products': products ,'cartItems':cartItems ,'favorites':favorites }
    return render(request,'store/store.html',context)



def cart(request):
    customor = request.session.get('customer')

    if not customor:
        request.session["customer"] = ''

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items ,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)


def checkout(request):
    customor = request.session.get('customer')

    if not customor:
        request.session["customer"] = ''

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order,'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updetefavorite(request):


    data = json.loads(request.body)
    productName = data['productName']
    action = data['action']
    customerId = request.session["customer"]

    product = Product.objects.get(name=productName)


    if action == 'addf':
        product.is_in_favorite=True
        product.save()
        favorite, created = Favorite.objects.get_or_create(customerId=customerId, product_name=productName)
        favorite.save()
    if action == 'removef':
        product.is_in_favorite = False
        product.save()
        favorite = Favorite.objects.get(customerId=customerId,product_name=productName)
        favorite.delete()

    return JsonResponse('Favorite was added', safe=False)

def updeteItem(request):
    customor = request.session.get('customer')

    if not customor:
        request.session["customer"] = ''

    data = json.loads(request.body)
    productId=data['productId']
    action = data['action']
    customerId = request.session["customer"]


    print('Action:', action)
    print('Product:', productId)
    print('customerId:', customerId)

    customer = Customer.objects.get(id=customerId)
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def processOrder(request):
    customor = request.session.get('customer')

    if not customor:
        request.session["customer"] = ''

    transaction_id =datetime.datetime.now().timestamp()

    data = json.loads(request.body)

    if request.session["customer"] != '':
        customerId = request.session["customer"]
        customer = Customer.objects.get(id=customerId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer,order=guestOrder(request,data)


    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            region=data['shipping']['region'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment Complete',safe=False)




def favorite(request):
    data = cartData(request)
    cartItems = data['cartItems']
    customorId=request.session["customer"]
    print('customor Id:',customorId)

    if customorId != '':
        favorits=Favorite.objects.all()
        products=Product.objects.all()

    fav_producs=[]

    for f in favorits:
        for p in products:
            if f.product_name == p.name and f.customerId == customorId:
                fav_producs.append(Product.objects.get(name=f.product_name))

    context = {'fav_items': fav_producs,'cartItems':cartItems}
    return render(request,'store/favorite.html',context)

def signup(request):

    return render(request, 'store/signup.html')

def profile(request):
    customorId = request.session["customer"]
    customor = Customer.objects.get(id=customorId)

    context={'customor':customor}
    return render(request, 'store/profile.html',context)

