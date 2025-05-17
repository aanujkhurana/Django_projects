from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        #authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If the user is authenticated, log them in
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            # If the authentication fails, show an error message
            messages.error(request, 'Invalid username or password.')
            return redirect('index')
    else:
        return render(request, 'index.html')

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('index')

