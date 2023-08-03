from django.db import models

class User(models.Model):
    """Пользователь"""
    name = models.CharField("Имя", max_length=15)
    surname = models.CharField("Фамилия", max_length=15)
    phone = models.CharField("Телефон", max_length=20)
    mail = models.CharField("Почта", max_length=30)
    login = models.CharField("Логин", max_length=30)
    password = models.CharField("Пароль", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Location(models.Model):
    """Локация"""
    name = models.CharField("Страна", max_length=15)
    surname = models.CharField("Город", max_length=15)
    phone = models.CharField("Улица", max_length=20)
    mail = models.CharField("Дом", max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"



# Create your models here.
