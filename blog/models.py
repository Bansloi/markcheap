from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from markcheap import settings
from tinymce.models import HTMLField
from blog.category import Category


from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    content = HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    draf = models.BooleanField(default=False)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f"/{self.slug}/"

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_reciever, sender=post)
