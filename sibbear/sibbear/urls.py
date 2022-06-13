from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from createusers.views import *
from django.conf.urls.static import static
urlpatterns = [
    path('', include('createusers.urls')),
    path('admin/', admin.site.urls),
    path('index/', include('createusers.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
