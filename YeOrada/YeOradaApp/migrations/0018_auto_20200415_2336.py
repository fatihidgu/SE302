# Generated by Django 3.0.4 on 2020-04-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YeOradaApp', '0017_auto_20200415_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentNumber',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likeNumber',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]