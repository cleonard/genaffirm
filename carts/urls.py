from django.urls import path

from . import views

app_name = "carts"

urlpatterns = [
    path("", views.listing, name="cart-listing"),
    path("create/", views.create, name="cart-create"),
    path("<str:token>", views.show, name="cart-show"),
    path("<str:token>/complete", views.complete, name="cart-complete"),
    # path("<str:token>/edit/", views.edit_cart, name="cart-edit"),
    # path("success/", views.success, name="checkout-success"),
    # path("cancel/", views.cancel, name="checkout-cancel"),
]
