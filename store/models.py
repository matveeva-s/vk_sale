from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class Item(models.Model):
    CREATED = 0
    BOOKED = 1
    SOLD = 2
    STATUS_CHOICES = [
        (CREATED, 'Добавлен'),
        (BOOKED, 'Забронирован'),
        (SOLD, 'Продан'),
    ]
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True)
    category = models.ForeignKey(
        to=Category, verbose_name='Категория', on_delete=models.SET_NULL, related_name='items', null=True, blank=True,
    )
    price_rub = models.IntegerField('Цена (рубли)', null=True, blank=True)
    price_coins = models.IntegerField('Цена (коины)', null=True, blank=True)
    status = models.SmallIntegerField('Статус', choices=STATUS_CHOICES, default=CREATED)
    seller = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, verbose_name='Продавец', on_delete=models.CASCADE, related_name='added_items'
    )
    buyer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, verbose_name='Покупатель', on_delete=models.SET_NULL, related_name='bought_items',
        null=True, blank=True,
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.title} ({self.seller.username})'


class ItemImage(models.Model):
    item = models.ForeignKey(to=Item, verbose_name='Товар', on_delete=models.CASCADE, related_name='images')
    order = models.IntegerField('Порядок фото', null=True, blank=True)
    image = models.ImageField(verbose_name='Фото', upload_to='item_images/', null=True)

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'

    def __str__(self):
        return f'{self.item.title} (№{self.order})'
