from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

from django.db.models import QuerySet

from .serializers import URLSerializer, HashURLSerializer
from shortener.models import URL

@api_view(["GET"])
def index(request):
    """
    Retreive `q` (url_hash) form path, and return the original url.
    """
    hash = request.GET.get("q", None)
    # print(f"\nhash: {hash}\n")
    if not hash:
        return Response(
            {}, 
            status=status.HTTP_204_NO_CONTENT
        )
    query_set: URL|None = None
    try:
        query_set = URL.objects.get(url_hash=hash)
    except:
        return Response(
            {},
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
        print(serializer.data)
        try:
            serializer.create(serializer.validated_data)
            return Response(
                serializer.data, 
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
                {},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
    else:
        return Response(
            {
                "error": "Invalid data"
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )
    return Response({}, status=status.HTTP_201_CREATED)