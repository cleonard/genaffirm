from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.


def main(request):
    # Redirect if already authed
    if request.user.is_authenticated:
        return redirect("carts:cart-listing")

    if request.method == "POST":
        # Form has been submitted
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("carts:cart-listing")

        messages.error(request, "Check your authentication credentials.")
    else:
        form = AuthenticationForm()

    return render(request, "authentication/index.html", {"form": form})


def sign_out(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("authentication:auth-main")


def stub_login(request):
    logout(request)
    user = User.objects.get(username="chris")
    login(request, user)
    return redirect("carts:cart-listing")
