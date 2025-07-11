from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('the_blues_brothers/contact/', views.contact_view, name='contact'),
    path('the_blues_brothers/members/', views.members, name='members'),
    path('the_blues_brothers/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]