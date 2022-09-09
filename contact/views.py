from django.shortcuts import render, redirect
from contact.models import contact
from django.contrib import messages

# Create your views here.


def contact_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        content = request.POST["content"]
        if len(name) < 2 or len(email) < 3 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            user = contact(name=name, email=email, content=content)
            user.save()
            messages.success(
                request,
                "Thank you for your message.We will answer your question as soon as possible.",
            )
            return redirect("contact")

    return render(request, "contact/contact.html")
