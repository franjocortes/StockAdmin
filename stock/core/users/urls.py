from django.urls import path

from .views import LoginFormView

app_name = 'users'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
]
