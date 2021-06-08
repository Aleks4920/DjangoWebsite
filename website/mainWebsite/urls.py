from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="site-home"),
    path("buy", views.Buy, name="buy"),
    path("sell", views.Sell, name="sell"),
    path("login", views.Login, name="login"),
    path("register", views.Register, name="register"),
    path("account", views.Account, name="account"),
    path("yourscripts", views.YourScripts, name="yourscripts"),
    path("settings", views.Settings, name="settings"),
]
