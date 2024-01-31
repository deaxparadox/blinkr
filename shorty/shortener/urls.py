from django.urls import path

from .views import (
    index_view,
    IndexView
)

app_name = "shortener"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
