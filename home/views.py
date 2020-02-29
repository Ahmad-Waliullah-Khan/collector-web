from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.conf import settings

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
        # find a way to pass books, movies, comics, games, shows related to the
        # user to the tempalte context object.
        # Later, paginate them

        return render(
            request, 'home/dashboard.html',
            {'books' : request.user.books.filter(user=request.user),
            'comics' : request.user.comics.filter(user=request.user),
            'games' : request.user.games.filter(user=request.user),
            'shows' : request.user.tv.filter(user=request.user),
            'movies' : request.user.movies.filter(user=request.user),
            }
        )
    else:
        return redirect("home:login")

@login_required
def logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home:login")
