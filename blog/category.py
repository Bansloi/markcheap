from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
