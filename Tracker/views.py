from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .models import *

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]

        #check for password strenght
        alphabets, nums, lower_case, upper_case = 0, 0, 0, 0
        for i in password:
            if i.isalpha():
                alphabets += 1
            if i.isnumeric():
                nums += 1
            if i.islower():
                lower_case += 1
            if i.isupper():
                upper_case += 1

        #If statemnts to give proper error 
        if len(password) < 8:
            return render(request, 'signup.html', {'message': 'Password must be aleast 8 characters long'})
        
        elif  alphabets < 1:
            return render(request, 'signup.html', {'message': 'Password must contain alphabets'})

        elif  nums < 1:
            return render(request, 'signup.html', {'message': 'Password must contain atleast 1 number'})

        elif  lower_case < 1:
            return render(request, 'signup.html', {'message': 'Password must contain atleast 1 lowercase alphabet'})

        elif  upper_case < 1:
            return render(request, 'signup.html', {'message': 'Password must contain atleast 1 UPPERCASE alphabet'})

        #check if passowd and confirm password are same
        elif password != c_password:
            return render(request, 'signup.html', {'message': 'Password must match.'})
        
        else:
            try:
                User.objects.get(username = username)
                return render(request, 'signup.html', {'message': 'Username already in use'})
            
            except User.DoesNotExist:

                try:
                    User.objects.get(email = email)
                    return render(request, 'signup.html', {'message': 'Email already in use.'})

                except User.DoesNotExist:
                    user = User.objects.create_user(username = username, first_name = name, email = email, password = password)
                    user.save()
                    login(request, user)
                    return redirect('landing')

        #trying to save data
        # try:
        #     user = User.objects.create_user(username = username, email = email, password = password)
        #     user.save()
        #     login(request, user)
        #     return redirect('landing')
        # except IntegrityError:
        #     return render(request, 'signup.html', {'message' : 'Username is already taken.'})

    else:
        return render(request, 'signup.html', {'message': ''})

def login_user(request):
    print('This is a test to check if the function is being called or not.')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        print('bhai data aa gya')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            return render(request, 'login.html', {'message': 'Please check the login credentials again.'})
    else:
        return render(request, 'login.html', {'message': ''})

def logout_user(request):
    logout(request)
    return redirect('landing')


@login_required
def dashboard(request):
    if request.method == "POST":
        if 'search' in request.POST:
            product_url = request.POST['product_url']

            try:
                URLS.objects.get(url = product_url)
                return render(request, 'dashboard.html', {'message': 'This product is already added'})

            except URLS.DoesNotExist:
                new_url = URLS(url = product_url)
                new_url.save()
                return render(request, 'dashboard.html', {'message': 'URL added successfully.'})

        if 'add2watchlist' in request.POST:
            pass
        
    user = request.user
    Wishlist = wishlist.objects.filter(user = user)

    if Wishlist:
        return render(request, 'dashboard.html', {'Wishlist': Wishlist})
    
    else:
        return render(request, 'dashboard.html', {'message': 'empty'})


def development(request):
    return render(request, 'development.html')