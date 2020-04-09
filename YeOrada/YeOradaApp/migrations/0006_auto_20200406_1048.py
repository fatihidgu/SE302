# Generated by Django 3.0.4 on 2020-04-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YeOradaApp', '0005_auto_20200406_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='category',
            field=models.CharField(blank=True, choices=[('RS', 'Restaurant'), ('CF', 'Cafe'), ('BR', 'Bar')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clientcuisine',
            name='cuisine',
            field=models.CharField(choices=[('RS', 'Kebap'), ('CF', 'Grill'), ('BR', 'Turkish'), ('BR', 'Pide'), ('BR', 'Döner'), ('BR', 'Fast Food'), ('BR', 'Homemade'), ('BR', 'Seafood'), ('BR', 'Cafe & Restaurant')], max_length=200),
        ),
    ]