# Generated by Django 3.0.4 on 2020-05-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YeOradaApp', '0021_auto_20200425_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_Approved',
            field=models.BooleanField(default=False),
        ),
    ]