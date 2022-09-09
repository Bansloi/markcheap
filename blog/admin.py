from django.contrib import admin
from django.db import models

from blog.models import post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "published"]
    search_fields = ["title", "published"]
    list_per_page = 10

    class Meta:
        models = post


admin.site.register(post, PostAdmin)
admin.site.register(Category)
