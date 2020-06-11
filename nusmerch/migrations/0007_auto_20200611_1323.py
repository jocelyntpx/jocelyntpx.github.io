# Generated by Django 3.0.6 on 2020-06-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusmerch', '0006_userinfo_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('imagefile', models.FileField(null=True, upload_to='images/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=200, unique=True, verbose_name='NUS Email'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='matric',
            field=models.CharField(help_text='AXXXXXXXB', max_length=10, unique=True, verbose_name='Matric Number'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='number',
            field=models.IntegerField(unique=True, verbose_name='Phone Number'),
        ),
    ]
