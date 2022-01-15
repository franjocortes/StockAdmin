from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from stock import settings


class LoginFormView(LoginView):
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)
