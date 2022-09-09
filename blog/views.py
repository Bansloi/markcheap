from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.core.paginator import Paginator
from blog.models import post
from blog.category import Category


# from blog.category import Category

# Create your views here.


def blog_view(request):
    posts = post.objects.all().order_by("-published")
    categories = Category.objects.all().order_by("-name")
    context = {"posts": posts, "categories": categories}
    return render(request, "blog/blog.html", context)


def details_view(request, slug=None):
    qs = get_object_or_404(post, slug=slug)
    context = {"blog": qs}
    return render(request, "blog/details.html", context)


def category_view(request, category):
    posts = post.objects.filter(category__name__cantains=category)
    context = {"posts": posts}
    return render(request, "blog/category.html", context)
