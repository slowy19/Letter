from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('accounts.urls')),
    path('chats/', include('chats.urls')),

    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('chats.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
