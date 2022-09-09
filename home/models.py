from django.db import models
from django.utils import timezone

# Create your models here.


class developer(models.Model):
    name = models.CharField(max_length=30)
    profile = models.ImageField(upload_to="img/")
    developer = models.CharField(max_length=30)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    last_login = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
