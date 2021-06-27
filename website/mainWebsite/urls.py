from django.urls import path
from . import views
from mainWebsite import views as core_views
urlpatterns = [
    path('', views.Buy, name="buy"),
    path("buy", views.Buy, name="buy"),
    path("sell", views.Sell, name="sell"),
    path("login", views.Login, name="login"),
    path("register", views.Register, name="register"),
    path("account", views.Account, name="account"),
    path("yourscripts", views.YourScripts, name="yourscripts"),
    path("settings", views.Settings, name="settings"),
    path("logout", views.Logout, name="logout"),
]
