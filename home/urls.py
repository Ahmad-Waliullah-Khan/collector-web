from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("logout/", views.logout, name="logout"),
]
