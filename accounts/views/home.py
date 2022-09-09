from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
from django.views import View
from django.contrib import messages


def home(request):
    count = User.objects.count()
    return render(request, "home/index.html", {"count": count})
