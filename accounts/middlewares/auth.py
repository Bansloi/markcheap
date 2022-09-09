from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.models import User


def auth_middleware(get_response):
    def my_function(request):
        if not request.session.get("user"):
            return redirect("login")

        response = get_response(request)
        return response

    return my_function
