from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def index(request):
    if request.user.is_anonymous:
        return redirect('/signup')
    return render(request, 'index.html')

def signupUser(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
            user.save()
            return redirect('/login')
        if password1!=password2:
            messages.error(request, 'Passwords Does Not Match')

    return render(request, 'signup.html')

def loginUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
