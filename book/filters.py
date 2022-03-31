import django_filters
from author.models import Author
from book.models import Book


class BookFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')
    authors = django_filters.ChoiceFilter(choices=list(map(lambda x: (x.id, f'{x.name} {x.surname}'), Author.get_all())))

    class Meta:
        model = Book
        fields = ['name', 'authors', ]
