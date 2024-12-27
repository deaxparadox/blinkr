from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode

def anonymous_user_view(request):
    if request.user.is_authenticated:
        return redirect("%s?%s" % (
            reverse("shortener:dashboard"),
            urlencode({"last":"no", "short_active": "no"})
        ))
    return render(request, "shortener/anonymous/index.html")
