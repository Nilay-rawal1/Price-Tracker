# Generated by Django 4.1.6 on 2023-02-08 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0003_price_history_product_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(unique=True),
        ),
        migrations.DeleteModel(
            name='URLS',
        ),
    ]