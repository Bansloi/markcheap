from django.contrib.sitemaps import Sitemap
from blog.models import post


# class PostSitemap(Sitemap):
#     def items(self):
#         return post.objects.all()


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return post.objects.all().order_by("-published")

    def lastmod(self, obj):
        return obj.updated
