from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password =  request.POST['password']
            post = User.objects.filter(username=username)
            if post:
                username = request.POST['username']
                user = authenticate(username=username, password=password)
                if user is not None:
                    request.session['username'] = username
                    return redirect("home:profile")
                else:
                    return render(request, 'home/login.html', {})
            else:
                return render(request, 'home/login.html', {})
    else:
        return redirect("home:profile")
    return render(request, 'home/login.html', {})

def profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts)
        return render(request, 'home/profile.html', {"query":query})
    else:
        return render(request, 'home/login.html', {})
