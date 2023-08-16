# Generated by Django 4.2.1 on 2023-08-14 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_carditem_count_alter_size_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'корзину', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='carditem',
            options={'verbose_name': 'карточку', 'verbose_name_plural': 'Карточки оплаты'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорию', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='cloth',
            options={'verbose_name': 'одежду', 'verbose_name_plural': 'Одежда'},
        ),
        migrations.AlterModelOptions(
            name='firm',
            options={'verbose_name': 'фирму', 'verbose_name_plural': 'Фирмы'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'платежку', 'verbose_name_plural': 'Платежки'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='shoes',
            options={'verbose_name': 'обувь', 'verbose_name_plural': 'Обувь'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'размер', 'verbose_name_plural': 'Размеры'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'Склад'},
        ),
    ]
