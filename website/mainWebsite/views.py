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
from .models import User, Post, Profile

#from .forms import ImageForm



def Buy(request):

    context = {
        'posts': Post.objects.all(),
        'title': 'Buy',
    }

    return render(request, 'mainWebsite/buy.html',context)


@login_required
@csrf_exempt
def Sell(request):
    if request.method == 'POST':
        obj = Post()
        #author
        obj.author = request.user
        #title
        obj.title = request.POST.get("title")
        #description
        obj.description = request.POST.get('description')
        #price
        obj.price = request.POST.get('price')
        #upload
        obj.upload = request.FILES.get('upload')
        #image
        obj.image = request.FILES.get('image')
        obj.save()


        context = {
            'posts': Post.objects.all(),
            'title': 'Buy',
        }

        return render(request, 'mainWebsite/buy.html',context)
    else:
        return render(request, 'mainWebsite/sell.html', {'title': 'Sell'})


def Register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mainWebsite/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "mainWebsite/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        profile = Profile()
        profile.user = user
        profile.save()
        return HttpResponseRedirect(reverse("buy"))
    else:
        return render(request, 'mainWebsite/register.html', {'title': 'Register'})


def Account(request):
    return render(request, 'mainWebsite/register.html', {'title': 'Account'})



def YourScripts(request):
    user = request.user
    if request.method == "POST":
        context = {
            'posts': Post.objects.all(),
            'title': 'Scripts',
            'value': request.POST.get('select')
        }

        return render(request, 'mainWebsite/yourscripts.html', context)

    else:
        context = {
            'posts': Post.objects.all(),
            'title': 'Scripts',
            'value':'All'
        }

        return render(request, 'mainWebsite/yourscripts.html', context)


def Settings(request):
    return render(request, 'mainWebsite/settings.html', {'title': 'Settings'})



#login
def Login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("buy"))
        else:
            return render(request, "mainWebsite/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, 'mainWebsite/login.html', {'title': 'Login'})

#logout
@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
