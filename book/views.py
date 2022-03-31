from django.views import generic

from book.filters import BookFilter
from book.models import Book


class BookListView(generic.ListView):

    model = Book
    context_object_name = "books"
    template_name = 'book/list.html'


class BookDetailView(generic.DetailView):

    model = Book
    context_object_name = "book"
    template_name = 'book/detail.html'


class UnorderedBookView(generic.ListView):

    context_object_name = 'books'
    template_name = 'book/list.html'
    extra_context = {"show_count": True}

    def get_queryset(self):

        return Book.objects.filter(count__gt=0)


class FilterBooksView(generic.TemplateView):

    template_name = 'book/filter.html'

    def get_context_data(self, **kwargs):
        context = super(FilterBooksView, self).get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=Book.objects.all())
        print(context['filter'].form)
        return context
