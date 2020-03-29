# Generated by Django 3.0.4 on 2020-03-29 18:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('YeOradaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.CharField(max_length=500)),
                ('rate', models.IntegerField()),
                ('clientEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YeOradaApp.Client')),
                ('customerEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YeOradaApp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YeOradaApp.Comment')),
                ('customerEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YeOradaApp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='CommentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=500)),
                ('commentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YeOradaApp.Comment')),
                ('customerEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YeOradaApp.Customer')),
            ],
        ),
    ]
