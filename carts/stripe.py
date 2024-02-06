import os

import stripe

BASE_DOMAIN = os.environ["BASE_DOMAIN"]


def create_stripe_session(cart_obj):
    stripe.api_key = os.environ["STRIPE_SECRET_KEY"]
    token = cart_obj.token

    # URLs: success_url and cancel_url
    success_url = f"{BASE_DOMAIN}carts/{token}/receipt?stripe_session_id={{CHECKOUT_SESSION_ID}}"
    cancel_url = f"{BASE_DOMAIN}carts/{token}?cancelled=true"

    session = stripe.checkout.Session.create(
        payment_method_types=["card", "affirm"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": f"Wellness Package - {token}"
                    },
                    "unit_amount": int(round(cart_obj.amount * 100)),
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url,
        metadata={"token": token},
    )

    return session
