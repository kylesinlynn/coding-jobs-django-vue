from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    return render(request, 'core/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
        
            return redirect('index')
    else:
        form = UserCreationForm()
        
    return render(request, 'core/signup.html', {'form': form})