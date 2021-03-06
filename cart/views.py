from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A veiw that renders the shopping cart contents """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of a product to the shopping cart """

    quantity = int(request.POST.get('amount'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def uppdate_cart(request, item_id):
    """ Edit quantity of a product to the shopping cart """

    quantity = int(request.POST.get('amount'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    cart[item_id] = quantity
    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart.pop(item_id)
    request.session['cart'] = cart

    return render(request, 'cart/cart.html')