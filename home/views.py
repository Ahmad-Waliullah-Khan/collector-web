from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

        books_list = request.user.books.filter(user=request.user)
        comics_list = request.user.comics.filter(user=request.user)
        games_list = request.user.games.filter(user=request.user)
        shows_list = request.user.tv.filter(user=request.user)
        movies_list = request.user.movies.filter(user=request.user)

        page = request.GET.get('page', 1)
        paginator = Paginator(movies_list, 6)
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)

        page = request.GET.get('page', 1)
        paginator = Paginator(books_list, 6)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)

        page = request.GET.get('page', 1)
        paginator = Paginator(comics_list, 6)
        try:
            comics = paginator.page(page)
        except PageNotAnInteger:
            comics = paginator.page(1)
        except EmptyPage:
            comics = paginator.page(paginator.num_pages)

        page = request.GET.get('page', 1)
        paginator = Paginator(games_list, 6)
        try:
            games = paginator.page(page)
        except PageNotAnInteger:
            games = paginator.page(1)
        except EmptyPage:
            games = paginator.page(paginator.num_pages)

        page = request.GET.get('page', 1)
        paginator = Paginator(shows_list, 6)
        try:
            shows = paginator.page(page)
        except PageNotAnInteger:
            shows = paginator.page(1)
        except EmptyPage:
            shows = paginator.page(paginator.num_pages)

        return render(
            request, 'home/dashboard.html',
            {'books' : books,
            'comics' : comics,
            'games' : games,
            'shows' : shows,
            'movies' : movies,
            }
        )
    else:
        return redirect("home:login")

@login_required
def logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home:login")
