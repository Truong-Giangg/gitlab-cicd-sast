from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

def _get_cart(request):
    return request.session.setdefault('cart', {})

def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = _get_cart(request)
    cart_item = cart.get(slug, {'qty': 0, 'price': str(product.price), 'name': product.name})
    cart_item['qty'] += 1
    cart[slug] = cart_item
    request.session['cart'] = cart
    return redirect('cart_view')

def remove_from_cart(request, slug):
    cart = _get_cart(request)
    if slug in cart:
        del cart[slug]
        request.session['cart'] = cart
    return redirect('cart_view')

def cart_view(request):
    cart = _get_cart(request)
    total = sum(float(item['price']) * item['qty'] for item in cart.values())
    return render(request, 'shop/cart.html', {'cart': cart, 'total': total})
