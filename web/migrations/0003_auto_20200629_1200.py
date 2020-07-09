# Generated by Django 3.1a1 on 2020-06-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='web/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]