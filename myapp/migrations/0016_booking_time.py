# Generated by Django 5.0.2 on 2024-03-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_booking_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Time',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
