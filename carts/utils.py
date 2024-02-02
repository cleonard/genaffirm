import os
import secrets

import stripe

TOKEN_LENGTH = 4


def create_stripe_session(product, urls):
    stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

    session = stripe.checkout.Session.create(
        payment_method_types=["card", "affirm"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": product["name"],
                    },
                    "unit_amount": product["amount"],
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=urls["success"],
        cancel_url=urls["cancel"],
    )

    return session


def unique_token(cls):
    while True:
        token = secrets.token_urlsafe(TOKEN_LENGTH)
        queryset = cls.objects.filter(token=token)
        if not queryset.exists():
            break
    return token
