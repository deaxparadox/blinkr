from typing import Any
from django.http import HttpRequest, HttpResponse, Http404
from django.views.decorators.http import require_POST, require_GET
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import (
    render, 
    get_object_or_404, 
    redirect,
)
from django.urls import path, reverse
from django.views.generic import ListView
from django.db import IntegrityError
from urllib.parse import urlencode

from authentication.models import Authentication, Setting
from shortener.models import URL, URLEncodeMedium
from shortener.form import URLForm


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
    # print(request.session.get("welcome", False))
    # print(request.session.keys())
    # print(request.META.get('HTTP_HOST', None))
    if request.user.is_authenticated:
        
        # Fetch query
        short_active = request.GET.get('short_active', None)
        last = request.GET.get('last', None)
        
        # If "short_active" and "last" not present in URL,
        # redirect to same URL with the same query parameter.
        # if not last and not short_active:
        #     return redirect(
        #         "%s?last=no&short_active=no" % reverse("shortener:dashboard")
        #     )
        
        
        
        # Get user
        user = None
        try:
            # user = User.objects.get(username=request.user.username)
            user = get_object_or_404(User, username=request.user.username)
        except Http404:
            messages.add_message(request, messages.DEBUG, "Unknown error: logged-in user error.")
    
        
        # If "last" and "short_active" are set to "yes",
        # include the last shorted URL for display
        last_url = None
        if last == "yes" and short_active == "yes":
            _last_url: URL = user.authentication.url.last()
            last_url = request.build_absolute_uri( 
                reverse("shortener:access", kwargs={"url_hash": _last_url.url_hash})
            )
            
        
        
        # url form    
        url_form = URLForm()
        
        # Session controlle welcome message.
        # 
        # After the welcome message is loaded, set 
        # "welcome" in session to False. It will not 
        # load the welcome message again.
        if not request.session.has_key("welcome"):
            messages.add_message(request, messages.INFO, "Welcome to URL Shortener")
            request.session['welcome'] = True
        
        
        return render(
            request,
            "shortener/dashboard.html",
            {
                "form": url_form,
                "last_url": last_url,
                "short_active": short_active
            }
        )
    
    
    return redirect(
        "%s?%s" % (
            reverse("authentication:login"),
            urlencode({"redirect_to": request.META.get("PATH_INFO")})
        )
    )
    # return redirect(reverse("authentication:login"))





# Hash url view
# 
# This url will receive a POST request with original url,
# to hash it. And will return up to Index view.
# 
def hash_url_view(request):
    
    # Check user authentication
    if request.user.is_authenticated:
        
        # Accept only POST request.    
        if request.method == "POST":
            
            # extract URLForm
            form = URLForm(request.POST)
            
            # validate URLForm
            if form.is_valid():
                
                # Step 1: Search the user, for Hash the URL.
                # Step 2: Hash the URL.
                # Step 3: Create ForeignKey.
                
                # Step 1
                try:
                    user = get_object_or_404(User, username=request.user.username)
                except Http404:
                    messages.add_message(request, messages.WARNING, "User not found.")
                    return redirect(reverse("shortener:dashboard"))
                
                # Step 2
                # Update `medium` field of medium
                new_url: URL = form.save(commit=False)
                new_url.medium = URLEncodeMedium.NORMAL
                new_url.save()
                
                # Step 3
                # Adding URL to authentication.
                user.authentication.url.add(new_url)
                

                # Return a successfull message. Redirecting to dashboard,
                # with new hash URL.
                messages.add_message(request, messages.SUCCESS, "URL hashed successfully.")
                return redirect(
                    "%s?%s" % (reverse("shortener:dashboard"), urlencode({"last": "yes", "short_active": "yes"}))
                ) 
            else:
                messages.add_message(request, messages.WARNING, form.errors)
                return redirect(reverse("shortener:dashboard"))
        else:
            return redirect(reverse("shortener:dashboard"))
    else:
        return redirect(reverse("authenication:login"))


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
    # print(request.build_absolute_uri())
    if request.user.is_authenticated:
        
        # History page rendering is done using,
        # template tag "history".
        
        return render(
            request,
            "shortener/history.html",
            {}
        )
    else:
        return redirect(
            "%s://%s%s?%s" % (
               request.scheme, 
               request.META.get("HTTP_HOST"),
               reverse("authentication:login"),
               urlencode({"redirect_to": request.META.get("PATH_INFO")})
            )
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