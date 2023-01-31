from django.contrib import admin
from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.routers import DefaultRouter


# Patterns of different paths
urlpatterns = [

    path('', views.home, name='home'),
    path('accounts/register/', views.registration, name='registration'),
    path('', include('django.contrib.auth.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'),
         name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('accounts/login/', views.user_login, name='login'),
]
