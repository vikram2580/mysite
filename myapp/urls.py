from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index,name='home'),

    path("about", views.about,name='about'),

    path("contact",views.contact,name='contact'),

    path("services",views.services,name='services'),

    path("signup",views.handleSignup,name='handleSignup'),

    path('login', views.handeLogin, name="handleLogin"),
    
    path('logout', views.handelLogout, name="handleLogout"),
    
]
