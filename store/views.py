from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from store.models import Item, ItemImage, Category
from store.pagination import ItemsPagination
from store.serializers import ItemListSerializer, ItemSerializer, CategorySerializer


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemsList(ListCreateAPIView): #LoginRequiredMixin
    # login_url = '/saml2/login/'
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    pagination_class = ItemsPagination

    def get_queryset(self):
        if self.kwargs.get('filter') == 'my':
            return self.queryset.filter(seller=self.request.user)
        return self.queryset

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category=category_id)
        return queryset


class ItemDetail(RetrieveUpdateAPIView): #LoginRequiredMixin
    # login_url = '/saml2/login/'
    queryset = Item.objects.all()
    lookup_field = 'pk'
    serializer_class = ItemSerializer


@api_view(['POST'])
def save_images(request, pk):
    item = get_object_or_404(Item, id=pk)
    images = request.FILES.getlist('images')
    for idx, image in enumerate(images):
        item_image = ItemImage.objects.create(item=item, image=image, order=idx)
        item_image.image.save(image.name, image, save=True)
    return Response({'msg': 'Ok'})
