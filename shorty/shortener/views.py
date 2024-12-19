from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST, require_GET
from django.contrib import messages
from django.shortcuts import (
    render, 
    get_object_or_404, 
    redirect,
)
from django.urls import path, reverse
from django.views.generic import ListView
from django.db import IntegrityError

from authentication.models import Authentication, Setting
from .models import URL, URLEncodeMedium
from .form import URLForm


# Index view
# 
# This view will be rendered to the logged in user.
# Display 5 latest hashed urls and a form to hash a
# new url
# 
def index_view(request):
    if request.user.is_authenticated:
        urls = URL.objects.all().order_by("-created")
        if len(urls) > 5:
            urls = urls[:5]
            
        form = URLForm()
        messages.add_message(request, messages.INFO, "Welcome to URL Shortener")
        return render(
            request,
            "shortener/index.html",
            {
                "urls": urls,
                "form": form
            }
        )
    return redirect(reverse("authentication:login"))


# Dashboard view
# 
# This view will be rendered to the logged in user.
# Display 5 latest hashed urls and a form to hash a
# new url
# 
def dashboard_view(request):
    # Check the request authentication.
    if request.user.is_authenticated:
        urls = URL.objects.all().order_by("-created")
        if len(urls) > 5:
            urls = urls[:5]
            
        form = URLForm()
        messages.add_message(request, messages.INFO, "Welcome to URL Shortener")
        return render(
            request,
            "shortener/dashboard.html",
            {
                "urls": urls,
                "form": form
            }
        )
    return redirect(reverse("authentication:login"))





# Hash url view
# 
# This url will receive a request with original url,
# to hash it. And will return up to Index view.
@require_POST
def hash_url_view(request):
    if request.user.is_authenticated():
        form = URLForm(request.POST)
        if form.is_valid():
            # Update `medium` field of medium
            model: URL = form.save(commit=False)
            model.medium = URLEncodeMedium.NORMAL
            model.save()
            

            messages.add_message(request, messages.SUCCESS, "URL hashed successfully.")
            return redirect(reverse("shortener:index")) 
    
    messages.add_message(request, messages.WARNING, form.errors)
    return redirect(reverse("shortener:index"))


class IndexView(ListView):
    model = URL
    template_name = "shortener/index_generic.html"


def access_view(request, url_hash: str|None = None):
    """
    This receives an argument called `url_hash` from the `URL` requested by a user. Inside the function, the first line tries to get the URL from the database using the `url_hash` argument. If not found, it returns the HTTP 404 error to the client, which means that the resource is missing. Afterwards, it increments the `clicked` property of the URL   entry, making sure to track how many times the URL is accessed. At the end, it redirects the client to the requested URL.

    The `root` View will be accessible in the `/` path of your server, accepting a `url_hash` as a string parameter.
    """
    # url_hash = request.GET.get("q", None)
    # if not url_hash:
    #     return redirect(reverse("shortener:index"))
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicked()

    return redirect(url.full_url)


@require_GET
def history_view(request):
    urls = URL.objects.all().order_by("-created_at")
    return render(
        request,
        "shortener/history.html",
        {
            "urls": urls
        }
    )
    
@require_GET
def view_search_view(request):
    q = request.GET.get("q", None)
    urls = None
    if q:
        # print(q)
        # print(q.strip().split(" "))
        # print(type(q))
        
        urls = URL.objects.all().order_by("-created_at")
        for k in q.split(" "):
            urls = urls.filter(full_url__contains=k)
        
        return render(
            request,
            "shortener/search.html",
            {
                "urls": urls,
            }
        )
    return render(
            request,
            "shortener/search.html",
            {
                "urls": urls,
            }
        )