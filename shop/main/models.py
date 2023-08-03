from django.db import models
from shop.user.models import User


class Firm(models.Model):
    """Фирма"""
    title = models.CharField("Наименование", max_length=15)


class Product(models.Model):
    """Фирма"""
    title = models.CharField("Наименование", max_length=50)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField("Цена", max_length=6)
    _HUMAN = [
        ('0', 'Для мужчин'),
        ('1', 'Для женщин'),
        ('2', 'Унисекс'),
    ]
    human = models.CharField(max_length=15, choices=_HUMAN, verbose_name="Для кого ?", default='0')


class Category(models.Model):
    """Категория"""
    title = models.CharField("Наименование", max_length=50)


class Cloth(models.Model):
    """Одежда"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)


class Size(models.Model):
    """размер"""
    title = models.IntegerField("Размер", max_length=6)


class Shoes(models.Model):
    """Обувь"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)


class Stock(models.Model):
    """Склад"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    count = models.IntegerField("Количество", max_length=5)


class Basket(models.Model):
    """Корзина"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    _STATUS = [
        ('0', 'Активен'),
        ('1', 'Неактивен'),
    ]
    status = models.CharField(max_length=15, choices=_STATUS, verbose_name="Статус", default='0')


class CardItem(models.Model):
    """CardItem"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, blank=True, null=True)
    count = models.IntegerField("Количество", max_length=5)
    sum = models.IntegerField("Количество", max_length=10)


class Order(models.Model):
    """Оплата"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, blank=True, null=True)
    _STATUS = [
        ('0', 'Передано на склад'),
        ('1', 'Загружается в машину'),
        ('2', 'В пути'),
        ('2', 'Доставлен'),
    ]
    status = models.CharField(max_length=15, choices=_STATUS, verbose_name="Статус", default='0')
    data = models.DateTimeField()
    data_pay = models.DateTimeField()
    _STATUS_PAY = [
        ('0', 'Не оплачен'),
        ('1', 'Оплачен'),
    ]
    status_pay = models.CharField(max_length=15, choices=_STATUS_PAY, verbose_name="Статус", default='0')
    sum = models.IntegerField("Количество", max_length=10)

# Create your models here.
