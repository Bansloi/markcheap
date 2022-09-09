from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
from django.views import View
from django.contrib import messages

from django.contrib.auth import login


class login(View):
    def get(self, request):
        return render(request, "login/login.html")

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.get_user_by_email(email)
        if user:
            bansloi = user.check_password(password)
            if bansloi:
                request.session["user"] = user.id
                return redirect("cheap")
            else:
                messages.error(request, "Provided email or password is not valid.")
                return redirect("login")
        else:
            messages.error(request, "Please Enter Valid Email or Password")
            return redirect("login")
