"""
URL configuration for shorty project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from .views import index_view

urlpatterns = [
    
    path("", index_view, name="index"),
    
    path(
        "shortener/", 
        include([
            path("api/", include("api.urls", namespace="api")),
            path("", include("shortener.urls", namespace="shortener")),
        ])
    ),
    
    
    
    # path(
    #     "",
    #     include([
    #         path("", index_view, name="index"),
    #         path("shortener/", include("shortener.urls", namespace="shortener")),
    #     ])
    # ),
    # path(
    #     "api/",
    #     include([
    #         path("", index_view, name="index"),
    #         path("shortener/", include("shortener.api.urls", namespace="shortener_api")),
    #     ])
    # ),

    # GraphQL path
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True)), name="shortener_graphql"),
] + [
    path('admin/', admin.site.urls),   
]
