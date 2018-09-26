from django.views.generic import TemplateView, ListView
from . models import Book

class AboutView(TemplateView):
    template_name = 'about.html'


class BooksList(ListView):
    model=Book
    template_name = 'books.html'
    context_object_name = 'books'