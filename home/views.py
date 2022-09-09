from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from home.models import developer

User = get_user_model()
from django.views import View
from django.contrib import messages


def home_view(request):
    count = User.objects.count()
    qs = developer.objects.all().order_by("-date_joined")[0:3]
    return render(request, "home/index.html", {"count": count, "post": qs})


def ads_view(request):
    return render(request, "home/ads.txt")


def favicon_view(request):
    return render(request, "home/favicon.ico")
