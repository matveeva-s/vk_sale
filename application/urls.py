from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_urls = [
    path('store/', include('store.urls', namespace='store_api')),
    path('users/', include('users.urls', namespace='users_api')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('saml2/', include('djangosaml2.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
