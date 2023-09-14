from django.urls import path, include
from .views import signup, activate
from . import views




urlpatterns = [
    # path("login/", views.LoginView.as_view(), name='login1'),
    path('', include('django.contrib.auth.urls')),
    path("registration/", signup, name='registration'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate, name='activate'),
]


