# Generated by Django 3.0.5 on 2020-04-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siberian_designs', '0002_auto_20200422_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='work',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
