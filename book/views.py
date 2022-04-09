from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404

from book.filters import BookFilter
from book.models import Book
from book.forms import BookForm


from rest_framework import viewsets
from book.serializers import RetrieveBookSerializer, BookSerializer


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


class SortedBookView(generic.ListView):

    template_name = 'book/sorted.html'
    context_object_name = 'books'

    def get_queryset(self):

        param = self.request.GET.get('param', '?')
        sorting = self.request.GET.get('sorting')
        queryset = Book.objects.order_by(param)

        if sorting == 'asc':
            return queryset
        return queryset.reverse()


class FilterBooksView(generic.TemplateView):

    template_name = 'book/filter.html'

    def get_context_data(self, **kwargs):
        context = super(FilterBooksView, self).get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=Book.objects.all())
        print(context['filter'].form)
        return context


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book/create_book.html', {'form': form})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/edit_book.html', {'form': form, 'pk': pk})


class BookAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RetrieveBookSerializer
        return BookSerializer


