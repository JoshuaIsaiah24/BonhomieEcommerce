# Generated by Django 5.0.1 on 2024-01-22 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
