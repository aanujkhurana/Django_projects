from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def index(request):
    search = request.GET.get('search') if request.GET.get('search') != None else ''
    records = Record.objects.filter(firstname__icontains=search)
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
        form = SignUpForm(request.POST or None)
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
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request, 'Record deleted successfully!')
        return redirect('index')
    else:
        messages.error(request, 'You must be logged in to delete a record.')
        return redirect('index')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added successfully!')
                return redirect('index')
            else:  
                return render(request, 'add_record.html', {'form': form})
        else:
            form = AddRecordForm()
            return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to add a record.')
        return redirect('index')
    
def edit_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=customer_record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record updated successfully!')
                return redirect('index')
            else:
                return render(request, 'edit_record.html', {'form': form})
        else:
            form = AddRecordForm(instance=customer_record)
            return render(request, 'edit_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to edit a record.')
        return redirect('index')