from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView


def index_view(request):
    return redirect(reverse("shortener:index"))

# class IndexView(ListView):
#     model: URL