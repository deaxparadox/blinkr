from django.urls import reverse
from django.shortcuts import render, redirect

def index_view(request):
    return redirect(reverse("shortener:index"))