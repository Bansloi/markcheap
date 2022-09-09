from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

from blog.feeds import LatestPostFeed
from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


admin.site.site_header = "Welcome To Markcheap"
admin.site.site_title = "Markcheap panel"
admin.site.index_title = "Markcheap admin"


# from accounts.views.home import home

from accounts.views.register import register
from accounts.views.login import login
from accounts.views.logout import logout_view
from accounts.views.forgot import forgot


sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include("home.urls")),
    url(r"^register/", register.as_view(), name="register"),
    url(r"^login/", login.as_view(), name="login"),
    url(r"^logout/", logout_view, name="logout"),
    url(r"^forgot-password/", forgot.as_view(), name="forgot"),
    url(r"^blog/", include("blog.urls")),
    url(r"^tinymce/", include("tinymce.urls")),
    url(r"^chat/", include("chat.urls")),
    url(r"^cheap/", include("cheap.urls")),
    url(r"^contact/", include("contact.urls")),
    url(r"^payment/", include("payments.urls")),
    url(r"^robots.txt/", include("robots.urls")),
    url(r"^sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    url(r"^feed/", LatestPostFeed(), name="post_feed"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
