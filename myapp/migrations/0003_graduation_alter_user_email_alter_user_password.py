# Generated by Django 5.0 on 2024-01-30 15:36

import django.core.validators
import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='graduation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, verbose_name=myapp.models.User)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator('Invalid email address')])),
                ('Address', models.CharField(max_length=200, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator('Invalid email address')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(8, 'Password must be at least 8 characters')]),
        ),
    ]
