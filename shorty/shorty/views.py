from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView



def index_view(request):
    if request.user.is_authenticated:
        return redirect(reverse("shortener:dashboard"))
    else:
        return redirect(reverse("authentication:login"))


def error_404(request):
    return render(request, "404.html", {})


def error_500(request):
    return render(request, "500.html", {})