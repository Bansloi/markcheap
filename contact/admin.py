from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from contact.models import contact

# Register your models here.


class contactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "timestamp"]
    search_fields = ["name", "email"]
    list_per_page = 10

    class Meta:
        model = contact


admin.site.register(contact, contactAdmin)
