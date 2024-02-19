from django.urls import path, include

from .views import (
    index_view,
    IndexView,
    root
)

app_name = "shortener"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("redirect/", root, name="root"),
]
