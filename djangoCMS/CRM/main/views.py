from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm
from .models import Record

# Create your views here.
def index(request):
    records = Record.objects.all()
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
        return render(request, 'index.html', {'records': records})
# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return render(request, 'index.html')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    
    return render(request, 'signup.html', {'form': form})
    

def record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'customer_record.html', {'customer_record': customer_record})
    else:
        messages.error(request, 'You must be logged in to view this page.')
        return redirect('index')