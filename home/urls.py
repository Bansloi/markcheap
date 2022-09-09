from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from home.views import home_view, ads_view, favicon_view

urlpatterns = [
    url(r"^$", home_view, name="home"),
    url(r"^ads.txt", ads_view, name="ads"),
    url(r"favicon.ico", favicon_view, name="favicon"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
