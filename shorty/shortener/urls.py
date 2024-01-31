from django.urls import path

from .views import (
    index_view,
    IndexView,
    root
)

app_name = "shortener"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<str:url_hash>/", root, name="root")
]
