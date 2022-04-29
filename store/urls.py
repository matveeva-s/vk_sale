from django.urls import path

import store.views as views

app_name = 'store'

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('items/', views.ItemsList.as_view(), name='items_list'),
    path('items/filtered/<slug:filter>/', views.ItemsList.as_view(), name='items-list-my'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='items_list'),
    path('items/<int:pk>/images_save/', views.save_images, name='images_save'),
]
