from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path("admin/", admin.site.urls),
    path("", include('admin_corporate.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
