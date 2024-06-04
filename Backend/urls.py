from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .routers import router

admin.site.site_header = 'RetiNode Administração'
admin.site.index_title = 'Administração'
admin.site.site_title = 'RetiNode'

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
