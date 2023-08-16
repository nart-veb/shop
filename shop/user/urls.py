from django.urls import path, include
from . import views



urlpatterns = [
    path("login/", views.LoginView.as_view(), name='login'),
    path("registration/", views.RegistrationView.as_view(), name='registration'),
]

