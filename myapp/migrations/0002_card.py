# Generated by Django 5.0 on 2024-01-27 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('card_num', models.BigIntegerField()),
                ('Cvv', models.IntegerField()),
                ('Expiry_Date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('Payment_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.payment')),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
