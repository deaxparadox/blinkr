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
from django.urls import path, include, re_path

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from . import views

urlpatterns = [
    
    
    path("api/", include("api.urls", namespace="api")),
    path("auth/", include("authentication.urls", namespace="authentication")),
    path("", include("shortener.urls", namespace="shortener")),
    
    # GraphQL path
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True)), name="shortener_graphql"),
] + [
    path('hidden/admin/', admin.site.urls),   
] + [
    # Page found
    re_path(r"^", views.error_404, name="error_404")
]
