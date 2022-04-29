# Generated by Django 4.0.4 on 2022-04-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='sys_id',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Id в sys'),
        ),
    ]