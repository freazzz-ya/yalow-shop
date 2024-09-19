from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('apps.orders.urls', namespace='catalog')),
    path('api/', include('apps.api.urls', namespace='api')),
    path('users/', include('apps.users.urls', namespace='users_list')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
