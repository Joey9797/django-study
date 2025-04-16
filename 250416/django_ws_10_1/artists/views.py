from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Artist
from .serializers import ArtistSerializer

@ api_view(['POST'])
def artist_list(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)