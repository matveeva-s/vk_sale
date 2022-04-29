from django.contrib import admin
from store.models import Item, ItemImage, Category


class ItemAdmin(admin.ModelAdmin):
    raw_id_fields = ('seller', 'buyer')
    search_fields = ('title',)
    model = Item


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class ItemImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('item',)
    model = ItemImage


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)
