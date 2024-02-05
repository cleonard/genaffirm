import secrets

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(unique=True)
    name = models.CharField()
    notes = models.TextField(blank=True)
    amount = models.PositiveIntegerField(default=0)
    stripe_session_id = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["token"]),
            models.Index(fields=["user_id"]),
        ]


def unique_token():
    while True:
        token = secrets.token_hex(4)
        check = Cart.objects.filter(token=token)
        if not check:
            return token
