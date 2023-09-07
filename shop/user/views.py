from django.shortcuts import render
from django.views.generic.base import View




class LoginView(View):
    # Страница авторизации
    def get(self, request):
        return render(request, 'shop/authorization.html')


class RegistrationView(View):
    # Страница регистрации
    def get(self, request):
        return render(request, 'shop/registration.html')









