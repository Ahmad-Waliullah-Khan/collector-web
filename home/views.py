from django.contrib.auth.models import User
from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        post = User.objects.filter(username=username)
        if post:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("profile")
        else:
            return render(request, 'home/login.html', {})
    return render(request, 'home/login.html', {})

def profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts)
        return render(request, 'home/profile.html', {"query":query})
    else:
        return render(request, 'home/login.html', {})
