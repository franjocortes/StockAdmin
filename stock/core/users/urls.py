from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import LoginFormView

app_name = 'users'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
