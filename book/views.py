from django.views import generic

from book.models import Book


class BookListView(generic.ListView):

    model = Book
    context_object_name = "books"
    template_name = 'book/list.html'


class BookDetailView(generic.DetailView):

    model = Book
    context_object_name = "book"
    template_name = 'book/detail.html'
