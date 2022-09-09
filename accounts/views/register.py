from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
from django.views import View
from django.contrib import messages


class register(View):
    def get(self, request):
        return render(request, "register/register.html")

    def post(self, request):
        name = request.POST["name"]
        email = request.POST["email"]
        email = email.lower()
        password = request.POST["password"]
        password2 = request.POST["password2"]

        # check the error
        if len(name) < 3 or len(email) < 3 or len(password) < 4:
            messages.error(request, "Please fill the form correctly")
            return redirect("register")

        if len(name) > 25 or len(email) > 50 or len(password) > 25:
            messages.error(request, "name 25, email 50, password 25 digit max!")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken!")
            return redirect("register")

        if password != password2:
            messages.error(request, "Your password do not match!")
            return redirect("register")
        else:
            c = User(name=name, email=email, password=password)
            c.password = make_password(c.password)

            c.save()
            messages.success(
                request, "congratulation your account is successfully created"
            )
            return redirect("login")
