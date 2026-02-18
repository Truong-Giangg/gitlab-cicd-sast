from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('product_list')
    total = sum(float(i['price']) * i['qty'] for i in cart.values())
    order = Order.objects.create(user=request.user, total=total)
    for slug, item in cart.items():
        # import here to avoid circular import at module load
        from shop.models import Product
        product = Product.objects.get(slug=slug)
        OrderItem.objects.create(order=order, product=product, price=item['price'], quantity=item['qty'])
    request.session['cart'] = {}
    return redirect('orders:thank_you')

def thank_you(request):
    return render(request, 'orders/thank_you.html')
