from django.shortcuts import render, redirect
from django.db.models import Avg, Count
from .forms import BookForm
from .models import  Book


def add_book(request):
    if request.method == "GET":
        f = BookForm()
        return render(request,'add_book.html', { 'form': f})
    else:
        f = BookForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/demo/list_books")
        else:
            return render(request, 'add_book.html', {'form': f})



def list_books(request):
    return render(request, 'list_books.html', {"books" : Book.objects.all()})

def book_home(request):
    context = Book.objects.all().aggregate(
           avgprice = Avg('price'), bookcount = Count('bookid'))

    return render(request, 'book_home.html', context)


def search_books(request):
    return render(request, 'search_books.html')