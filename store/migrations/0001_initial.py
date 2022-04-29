# Generated by Django 4.0.4 on 2022-04-23 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price_rub', models.IntegerField(null=True, blank=True, verbose_name='Цена (рубли)')),
                ('price_coins', models.IntegerField(null=True, blank=True, verbose_name='Цена (коины)')),
                ('status', models.SmallIntegerField(choices=[(0, 'Добавлен'), (1, 'Забронирован'), (2, 'Продан')], default=0, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bought_items', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_items', to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Порядок фото')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.item', verbose_name='Товар')),
                ('image', models.ImageField(verbose_name='Фото', null=True, upload_to='media/',))
            ],
            options={
                'verbose_name': 'Фото товара',
                'verbose_name_plural': 'Фото товаров',
            },
        ),
    ]