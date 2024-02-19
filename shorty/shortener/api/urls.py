from django.urls import path, include, re_path

from shortener.api import views

app_name = "shortener_api"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create")
]
