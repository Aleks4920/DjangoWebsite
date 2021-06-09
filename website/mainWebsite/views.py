from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from .models import Post






def Buy(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Buy',
    }

    return render(request, 'mainWebsite/buy.html',context)

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
