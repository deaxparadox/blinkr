from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views.generic import ListView

from .models import URL

def index_view(request):
    return render(
        request,
        "shortener/index.html"
    )


class IndexView(ListView):
    model = URL
    template_name = "shortener/index_generic.html"