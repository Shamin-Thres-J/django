from django.urls import path
from .import views

urlpatterns = [
    path("", views.intro ,name='intro'),
    path('homepage/', views.homepage, name='homepage'),
    path('bot/', views.bot, name='bot'),
    path('about/', views.about, name='about' ),
    path('login/', views.Login, name='login'),
    path('members/', views.members, name='members'),
    path('logout/', views.Logout, name='logout'),
    path('home/', views.Home, name='home'),
    path('post/', views.Post, name='post'),
    path('messages/', views.Messages, name='messages'),
    path('test/', views.test, name='test'),
    path('contact/', views.contact, name='contact'),
   

]