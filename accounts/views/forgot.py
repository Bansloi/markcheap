from django.shortcuts import redirect, render
from markcheap import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib import messages
from django.core.mail import send_mail
from django.views import View


class forgot(View):
    def get(self, request):
        return render(request, "forgot/forgot.html")

    def post(self, request):
        email = request.POST["email"]
        if len(email) < 2:
            messages.error(request, "Please Enter Your Email-id ")
            return redirect("forgot")
        f = User.get_user_by_email(email)
        if f:
            messages.success(
                request, "Please check your email for a link to reset your password."
            )
            return redirect("forgot")
            subject = "bansloi member"
            msg = "congratulations"
            to = "pithalapur@gmail.com"
            res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
            if res == 1:
                msg = "Mail send"
            else:
                msg = "Mail could not send"
        else:
            messages.error(request, "This email is not registred")
            return redirect("forgot")
