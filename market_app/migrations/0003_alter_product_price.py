# Generated by Django 5.1.6 on 2025-02-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_app', '0002_market_product_seller_delete_customer_product_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
