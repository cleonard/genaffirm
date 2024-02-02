import datetime
import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from carts.forms import CartForm
from carts.models import Cart, unique_token
from carts.stripe import create_stripe_session

# Create your views here.


@login_required
def listing(request):
    """Home/default view when authed - list user's existing carts"""
    carts = Cart.objects.all()
    context = {"carts": carts}
    return render(request, "carts/index.html", context=context)


@login_required
def create(request):
    if request.method == "POST":
        # New obj
        form = CartForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            notes = form.cleaned_data["notes"]
            amount = form.cleaned_data["amount"]
            cart = Cart(name=name, notes=notes, amount=amount)
            cart.user = request.user
            cart.token = unique_token()
            cart.save()

            # Redirect
            return redirect(request, "carts:cart-show", cart.token)
    else:
        form = CartForm()

    context = {"form": form}
    return render(request, "carts/create.html", context=context)


@login_required
def show(request, token):
    cart = Cart.objects.get(token=token)
    stripe_session = create_stripe_session(cart)
    stripe_pk = os.environ["STRIPE_PUBLISHABLE_KEY"]
    context = {
        "cart": cart,
        "stripe_session": stripe_session,
        "publishable_key": stripe_pk,
    }
    return render(request, "carts/show.html", context=context)


@login_required
def complete(request, token):
    ...
