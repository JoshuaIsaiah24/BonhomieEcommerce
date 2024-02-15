from django.shortcuts import render, redirect
from store.models import Product
from cart.models import Cart

# Create your views here.

def cart_details(request):
    cart_items = Cart.objects.filter(user=request.user.id)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    context = {
        
        'cart_items': cart_items,
        'total_price': total_price,
        
            }
    
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = Cart.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('cart')