from rest_framework.response import Response
from demo.models import Book
from demo.serializers import BookSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def list_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


def process_book(request):
    pass

