# Generated by Django 3.0.6 on 2020-06-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusmerch', '0027_auto_20200619_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='Product Description'),
        ),
    ]