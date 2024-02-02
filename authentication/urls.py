from django.urls import path

from . import views

app_name = "authentication"

urlpatterns = [
    path("", views.main, name="auth-main"),
    path("logout/", views.sign_out, name="auth-signout"),
    path("__stub__/", views.stub_login, name="auth-stub")
]
