# Generated by Django 3.0.6 on 2020-06-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusmerch', '0010_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]