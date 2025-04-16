from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookListSerializer, BookSerializer
from .models import Book


@ api_view(['GET'])
def libraries(request):
    books = Book.objects.all()
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)
