from rest_framework.response import Response
from django.shortcuts import render
from demo.models import Book
from demo.serializers import BookSerializer
from rest_framework.decorators import api_view


def client(request):
    return render(request, "rest_client.html")


@api_view(['GET', 'POST'])
def list_books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        print(serializer.data)
        return Response(serializer.data)
    else:  # Post
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Insert row into table
            return Response(serializer.data, status=201)  # Successful post

        return Response(serializer.errors, status=400)  # Invalid data, return bad request


@api_view(['GET', 'DELETE', 'PUT'])
def process_book(request, bookid):
    try:
        book = Book.objects.get(bookid=bookid)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':  # Update
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response(serializer.data)

        return Response(serializer.errors, status=400)  # Response is bad request
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=204)
