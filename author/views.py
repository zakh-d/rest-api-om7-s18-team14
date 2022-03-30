from django.views import generic

from author.models import Author


class AuthorListView(generic.ListView):

    model = Author
    context_object_name = "authors"
    template_name = 'author/list.html'


class AuthorDetailView(generic.DetailView):

    model = Author
    context_object_name = "author"
    template_name = 'author/detail.html'
