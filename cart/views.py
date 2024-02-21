from django.shortcuts import render,redirect,get_object_or_404
from demoapp.models import Product
from.models import Cart
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def addcart(req,id):
    print(id)
    user=req.session['user']
    product=Product.objects.get(id=id)
    print(product)
    try:
        cartItem=Cart.objects.get(user=user,product=product)
        if cartItem.quantity<cartItem.product.stock:
            cartItem.quantity+=1
            cartItem.save()
    except Cart.DoesNotExist:
        cartItem=Cart.objects.create(user=user,product=product,quantity=1)
        cartItem.save()
    return redirect('cart:displaycart')


def displaycart(req):
    user=req.session['user']
    cart=Cart.objects.all().filter(user=user)
    return render(req,'cart.html',{'cart':cart})

def remove(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(user=user,product=product)
    cart.delete()
    return redirect('cart:displaycart')


def reduce(req,id):
    user=req.session['user'] 
    product=get_object_or_404 (Product,id=id)
    cartItem=Cart.objects.get(user=user,product=product)
    if cartItem.quantity > 1:
        cartItem.quantity-=1
        cartItem.save()
    else:
        cartItem.delete()
        
    return redirect('cart:displaycart')
def placeorder(req,id):
    user=req.session['user'] 
    cartItem=Cart.objects.all().filter(user=user)
    cartItem.delete()
    
    return redirect('cart:displaycart')