from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('proyectos.urls')),  # Carga las URLs de tu app principal
    path('api-auth/', include('rest_framework.urls')),
]

# 🔽 Servir archivos multimedia en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
