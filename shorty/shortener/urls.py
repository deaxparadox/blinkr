from django.urls import path, include

from shortener.views.auth import (
    index_view,
    hash_url_view,
    IndexView,
    access_view,
    history_view,
    view_search_view,
    dashboard_view
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
    
    
    # Anonymous users paths is specified in shorty/views.py
    path("", anonymous_user_view, name="anonymous")
]
