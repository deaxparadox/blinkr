from django.urls import path, include, re_path

from shortener.views.auth import (
    index_view,
    hash_url_view,
    IndexView,
    access_view,
    history_view,
    view_search_view,
    dashboard_view
)
from shortener.views.redirect import (
    dashboard_view_redirect,
    history_view_redirect
)
from shortener.views.anonymous import anonymous_user_view

app_name = "shortener"


urlpatterns = [
    # Authenticated users
    path("dashboard/", dashboard_view, name="dashboard"),
    path("search/", view_search_view, name="search"),
    path("hash/", hash_url_view, name='hash'),
    path("history/", history_view, name='history'),
    path("<str:url_hash>/", access_view, name="access"),
    
    
    # redirect views to proper path
    re_path(r"^dashboard$", dashboard_view_redirect, name="dashboard_redirect"),
    re_path(r"^history$", history_view_redirect, name="history_redirect"),
    
    # Anonymous users paths is specified in shorty/views.py
    path("", anonymous_user_view, name="anonymous")
]
