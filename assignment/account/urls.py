from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    ProfileView,
    ProfileUpdateView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),

    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='account/change_password/change_password.html',
            success_url='/'
        ),
        name='change-password'
    ),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/change_password/password_reset.html'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/change_password/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/change_password/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/change_password/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),


]