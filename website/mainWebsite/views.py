from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'mainWebsite/layout.html', {'title': 'Main'})

def Buy(request):
    return render(request, 'mainWebsite/buy.html', {'title': 'Buy'})

def Sell(request):
    return render(request, 'mainWebsite/sell.html', {'title': 'Sell'})

def Login(request):
    return render(request, 'mainWebsite/login.html', {'title': 'Login'})

def Register(request):
    return render(request, 'mainWebsite/register.html', {'title': 'Register'})


def Account(request):
    return render(request, 'mainWebsite/register.html', {'title': 'Account'})


def YourScripts(request):
    return render(request, 'mainWebsite/yourscripts.html', {'title': 'Scripts'})

def Settings(request):
    return render(request, 'mainWebsite/settings.html', {'title': 'Settings'})
