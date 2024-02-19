from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from django.db.models import QuerySet


from shortener.api.serializers import URLSerializer, HashURLSerializer
from shortener.models import URL

@api_view(["GET"])
def index(request):
    
    hash = request.GET.get("q", None)
    print(f"\nhash: {hash}\n")
    if not hash:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    query_set: URL|None = None
    try:
        query_set = URL.objects.get(url_hash=hash)
    except:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    serializer = URLSerializer(query_set)
    return Response(serializer.data, status=status.HTTP_200_OK)

    
@api_view(["POST"])
def create(request):
    serializer = HashURLSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
    return Response({}, status=status.HTTP_201_CREATED)