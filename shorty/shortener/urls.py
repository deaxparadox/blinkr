from django.urls import path, include

from .views import (
    index_view,
    hash_url_view,
    IndexView,
    access_view,
    history_view,
    view_search_view,
    dashboard_view
)

app_name = "shortener"


urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard"),
    path("search/", view_search_view, name="search"),
    path("hash/", hash_url_view, name='hash'),
    path("history/", history_view, name='history'),
    path("<str:url_hash>/", access_view, name="access"),
    path("", index_view, name="index"),
]
