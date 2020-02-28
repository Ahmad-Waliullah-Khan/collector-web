from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login

def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password =  request.POST['password']
            post = User.objects.filter(username=username)
            if post:
                username = request.POST['username']
                user = authenticate(request, username=username, password=password)
                if user:
                    auth_login(request, user)
                    request.session['username'] = username
                    return redirect("home:dashboard")
                else:
                    return render(request, 'home/login.html', {})
            else:
                return render(request, 'home/login.html', {})
        else:
            if request.user.is_authenticated:
                return redirect("home:dashboard")
        return render(request, 'home/login.html', {})

@login_required
def profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts)
        return render(request, 'home/profile.html', {"query":query})
    else:
        return render(request, 'home/login.html', {})

@login_required
def dashboard(request):
    if request.user.is_authenticated:

        return render(request, 'home/dashboard.html', {})
    else:
        return redirect("home:login")

@login_required
def logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home:login")
