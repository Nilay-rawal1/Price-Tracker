from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

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
        if password != c_password:
            return render(request, 'signup.html', {'message': 'Password must match.'})
        
        #trying to save data
        try:
            user = User.objects.create_user(username = username, name = name, email = email, password = password)
            user.save()
            login(request, user)
            return redirect('landing')
        except IntegrityError:
            return render(request, 'signup.html', {'message' : 'Username is already taken.'})

    else:
        return render(request, 'signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print('bhai data aa gya')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            return render(request, 'login.html', {'message': 'Please check the login credentials again.'})
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('landing')