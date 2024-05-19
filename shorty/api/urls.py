from django.urls import path, include, re_path

from . import views

app_name = "shortener_api"

urlpatterns = [
    path("endpoints/", views.endpoints_view, name="endpoints"),
    path("create/", views.create, name="create"),
    path("", views.index, name="index"),
    
]
