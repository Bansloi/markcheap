from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


from blog.views import blog_view, details_view, category_view

urlpatterns = [
    url(r"^$", blog_view, name="blog"),
    url(r"^(?P<slug>[\w-]+)/$", details_view, name="detail"),
    url(r"^(?P<slug>[\w-]+)$/", category_view, name="category"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
