from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy
from .forms import MyUserCreationForm


class MyLoginView(LoginView):
    template_name = "login.html"


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class MyPasswordChangeView(PasswordChangeView):
    template_name = "password_change_form.html"
    success_url = reverse_lazy("password_change_done")


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "password_change_done.html"


class MyPasswordResetView(PasswordResetView):
    template_name = "password_reset_form.html"
    success_url = reverse_lazy("password_reset_done")


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = reverse_lazy("password_reset_done.html")


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "password_reset_confirm.html"
    success_url = reverse_lazy("password_reset_complete")


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = reverse_lazy("password_reset_complete.html")
