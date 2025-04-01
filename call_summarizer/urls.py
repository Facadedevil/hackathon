from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from audio_processor.views import generate_summary

urlpatterns = [
    path('', generate_summary, name='generate_summary'),  # Root becomes the endpoint
    path('admin/', admin.site.urls),
    path('api/', include('audio_processor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)