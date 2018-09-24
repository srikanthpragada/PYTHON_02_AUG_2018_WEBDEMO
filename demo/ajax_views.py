from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from datetime import datetime, time
import time
from .models import Book


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def now(request):
    # time.sleep(10)
    return HttpResponse(str(datetime.now()))


def get_title(request):
    id = request.GET["bookid"]
    print(id)

    try:
        book = Book.objects.get(bookid=id)
        title = book.title;
    except:
        title = "Book Not Found"

    return HttpResponse(title)


def get_book(request):
    id = request.GET["bookid"]
    try:
        book = Book.objects.get(bookid=id)
        return JsonResponse({"title" : book.title, "price" : book.price, "author": book.author}, safe=False)
    except:
        return JsonResponse({"error" : "Book not found!"})
