from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def signup(request):
    return render(request, 'core/signup.html')