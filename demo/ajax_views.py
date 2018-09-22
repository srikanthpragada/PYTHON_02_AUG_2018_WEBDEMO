from django.shortcuts import render
from django.http import HttpResponse
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
    book = Book.objects.get(bookid = id)
    return HttpResponse(book.title)
