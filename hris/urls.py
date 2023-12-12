import document as document
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('leaves.urls')),
    path('attendance/',include('attendance.urls')),
    path('account/',include('account.urls')),
    path('authentication/',include('authentication.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)