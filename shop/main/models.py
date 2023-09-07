from django.db import models
from user.models import User


class Firm(models.Model):
    """Фирма"""
    title = models.CharField("Наименование", max_length=15)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "фирму"
        verbose_name_plural = "Фирмы"


class Category(models.Model):
    """Категория"""
    title = models.CharField("Наименование", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"


class Size(models.Model):
    """размер"""
    title = models.CharField("Размер", max_length=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "размер"
        verbose_name_plural = "Размеры"


class Product(models.Model):
    """Товар"""
    title = models.CharField("Наименование", max_length=50)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name='Фирма')
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField("Картинка", upload_to="images_product/")
    _HUMAN = [
        ('Для мужчин', 'Для мужчин'),
        ('Для женщин', 'Для женщин'),
        ('Унисекс', 'Унисекс'),
    ]
    human = models.CharField(max_length=15, choices=_HUMAN, verbose_name="Для кого ?", default='Для мужчин')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"


class Cloth(models.Model):
    """Одежда"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "одежду"
        verbose_name_plural = "Одежда"


class Shoes(models.Model):
    """Обувь"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "обувь"
        verbose_name_plural = "Обувь"


class Stock(models.Model):
    """Склад"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    count = models.IntegerField("Количество")

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Склад"


class Basket(models.Model):
    """Корзина"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.BooleanField(verbose_name="Статус", default=False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "корзину"
        verbose_name_plural = "Корзины"


class CardItem(models.Model):
    """CardItem"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    count = models.IntegerField("Количество")
    sum = models.DecimalField(decimal_places=2, max_digits=2)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = "карточку"
        verbose_name_plural = "Карточки оплаты"


class Order(models.Model):
    """Оплата"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    _STATUS = [
        ('0', 'Передано на склад'),
        ('1', 'Загружается в машину'),
        ('2', 'В пути'),
        ('2', 'Доставлен'),
    ]
    status = models.CharField(max_length=15, choices=_STATUS, verbose_name="Статус", default='0')
    data = models.DateTimeField()
    data_pay = models.DateTimeField()
    status_pay = models.BooleanField(verbose_name="Статус", default=False)
    sum = models.DecimalField(decimal_places=2, max_digits=2)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "платежку"
        verbose_name_plural = "Платежки"

# Create your models here.
