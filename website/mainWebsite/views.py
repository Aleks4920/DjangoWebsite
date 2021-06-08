from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'mainWebsite/layout.html')

def Buy(request):
    return render(request, 'mainWebsite/buy.html')

def Sell(request):
    return render(request, 'mainWebsite/sell.html')

def Login(request):
    return render(request, 'mainWebsite/login.html')

def Register(request):
    return render(request, 'mainWebsite/register.html')


def Account(request):
    return render(request, 'mainWebsite/register.html')


def YourScripts(request):
    return render(request, 'mainWebsite/yourscripts.html')

def Settings(request):
    return render(request, 'mainWebsite/settings.html')
