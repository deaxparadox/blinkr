from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse

from django.db.models import QuerySet
from django.db import DatabaseError

from .serializers import URLSerializer, HashURLSerializer
from shortener.models import URL

@api_view(["GET"])
def index(request):
    """
    if `q` is None, then return all urls, default to `all`
    
    if `q` is url hash, return original url of url.
    """
    hash = request.GET.get("q", None)
    
    if not hash or hash == "all":
        urls = URL.objects.all()
        serializer = URLSerializer(urls, many=True)
        return Response(
            serializer.data, 
            status=status.HTTP_204_NO_CONTENT
        )
    
    query_set: URL|None = None
    try:
        query_set = URL.objects.get(url_hash=hash)
    except URL.DoesNotExist as e:
        print(str(e), type(e))
        return Response(
            {"error": str(e)},
            status=status.HTTP_204_NO_CONTENT
        )
    serializer = URLSerializer(query_set)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

    
@api_view(["POST"])
def create(request):
    """
    `full_url` will received as the form data, and 
    serializer will create new database object.
    
    If: similar url already exists, raise DB `InterityError`,
    and return `CONFICT` status, with error message.
    
    If: serializer is invalid then return, `BAD_REQUEST` status,
    with error message.
    
    If: any other error is raise, Exception will catch the error, 
    and return `NOT ACCEPTABLE` error.
    """
    
    serializer = HashURLSerializer(data=request.data)

    
    if serializer.is_valid():
        try:
            
            # check for URL existence
            urls = URL.objects.filter(full_url=serializer.validated_data.get('full_url'))
            if len(urls) > 0:
                # URL exist
                query_set = urls[0]
            else:
                # URL not exist, create new hash
                query_set = serializer.create(serializer.validated_data)
            
            # print(
            #     "Data:", 
            #     query_set.url_hash
            # )
            
            ret = {
                "hash": request.build_absolute_uri(reverse("shortener:access", kwargs={"url_hash": query_set.url_hash}))
            }
            ret.update({"full_url": serializer.data.get("full_url")})
            return Response(
                ret, 
                status=status.HTTP_201_CREATED
            )
        except IntegrityError as e:
            return Response(
                {
                    "error": str(e)
                }, 
                status=status.HTTP_409_CONFLICT
            )
        except Exception as e:
            return Response(
                { "error": str(e) },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
    return Response(
        {
            "error": "Invalid data"
        }, 
        status=status.HTTP_400_BAD_REQUEST
    )


def endpoints_view(request):
    if request.user.is_authenticated:    
        return render(
            request,
            "api/index.html"
        )
    return redirect(reverse("authentication:login"))