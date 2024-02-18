"""Urls for user loging"""
from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
# from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('signup/', views.signup, name='users-sign-up'),
    path('profile/', views.profile, name='users-profile'),
    path('', auth_view.LoginView.as_view(template_name='users/login.html'),
         name='users-login'),
    path('logout/', views.logout_view, name='users-logout'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'), # first stage
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),  # second stage
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'), # third stage
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),  # 4th stage.

]
