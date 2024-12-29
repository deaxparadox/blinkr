from django.shortcuts import redirect
from django.urls import reverse

def dashboard_view_redirect(request):
    return redirect(reverse("shortener:dashboard"))


def history_view_redirect(request):
    return redirect(reverse("shortener:history"))