from django.views import generic
from django.shortcuts import render, redirect

from author.models import Author
from .forms import AuthorCreationForm


class AuthorListView(generic.ListView):

    model = Author
    context_object_name = "authors"
    template_name = 'author/list.html'


class AuthorDetailView(generic.DetailView):

    model = Author
    context_object_name = "author"
    template_name = 'author/detail.html'

def create_author(request):
    # form = AuthorCreationForm()
    if request.method == "POST":
        form = AuthorCreationForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('author_detail', pk=post.pk)
    else:
        form = AuthorCreationForm()

    return render(request, 'author/create_author.html', {'form': form})
