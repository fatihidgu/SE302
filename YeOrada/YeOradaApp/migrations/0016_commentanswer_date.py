# Generated by Django 3.0.4 on 2020-04-15 17:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('YeOradaApp', '0015_customer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentanswer',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
