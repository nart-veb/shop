# Generated by Django 4.2.1 on 2023-08-14 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_size_alter_size_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
