# Generated by Django 4.2.1 on 2023-08-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_basket_user_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='images_product/', verbose_name='Картинка'),
            preserve_default=False,
        ),
    ]
