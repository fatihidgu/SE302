# Generated by Django 3.0.4 on 2020-05-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YeOradaApp', '0030_clientapplicationform_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='workingDaysFrom',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='workingDaysTo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='workingHoursFrom',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='workingHoursTo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
