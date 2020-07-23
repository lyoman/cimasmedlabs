from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (register_patient, home_page, registration_redirect, redirect_logged, dashboard, about, contact)

app_name = 'users'
urlpatterns = [
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('password-reset/',auth_views.PasswordResetView.as_view(template_name='reset/password_reset_form.html'),name='password_reset'),
        path('users/password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'),name='password_reset_done'),
        path('users/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_confirm.html'),name='password_reset_confirm'),
        path('users/reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'),name='password_reset_complete'),
        path('dash/',redirect_logged, name='dash'),
        path('admin/',  dashboard , name='dashboard'), 
        path('register/patient/', register_patient, name='register_patient'),
        path('register/', registration_redirect , name='registration_redirect'),
        path('aboutus/', about, name='about'),
        path('contact/', contact, name='contact'),
        path('', home_page, name='home_page'),
]