from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'signup.html')