# Generated by Django 3.0 on 2020-01-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
