# Generated by Django 4.0.3 on 2022-04-08 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deal',
            options={'verbose_name': 'Сделки', 'verbose_name_plural': 'Deals'},
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Настройки', 'verbose_name_plural': 'Settings'},
        ),
        migrations.AlterModelOptions(
            name='summary',
            options={'verbose_name': 'Сводка', 'verbose_name_plural': 'Summaries'},
        ),
    ]
