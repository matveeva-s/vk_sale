from rest_framework import serializers

from users.serializers import UserSerializer

from store.models import Item, ItemImage, Category
from django.conf import settings


class ItemImageSerializer(serializers.ModelSerializer):
    # image = serializers.URLField()

    class Meta:
        model = ItemImage
        fields = ('id', 'image', 'order')

    # @staticmethod
    # def get_image(obj):
    #     return obj.image and settings.DOMAIN + obj.image.url


class ItemListSerializer(serializers.ModelSerializer):
    seller = UserSerializer(required=False)
    preview = serializers.SerializerMethodField()
    description = serializers.CharField()
    images = ItemImageSerializer(many=True, read_only=True)
    category = serializers.SerializerMethodField()

    def get_category(self, item):
        return getattr(item.category, 'name', None)

    def get_preview(self, item):
        if item.images.exists():
            return item.images.first().image.url
            # return settings.DOMAIN + item.images.first().image.url
        return ''

    def create(self, validated_data):
        validated_data['seller'] = self.context['request'].user
        categories = Category.objects.filter(name=self.context['request'].data['category']['name'])
        self.instance = super(ItemListSerializer, self).create(validated_data)
        if categories.exists():
            self.instance.category = categories.first()
        self.instance.save()
        return self.instance

    class Meta:
        model = Item
        fields = (
            'id', 'title', 'description', 'preview', 'price_rub', 'price_coins', 'status', 'seller', 'images', 'category'
        )


class ItemSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    buyer = UserSerializer()
    images = ItemImageSerializer(many=True)

    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'images', 'price_rub', 'price_coins', 'status', 'seller', 'buyer')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
