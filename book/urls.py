from django.urls import path
from book.views import BookListView

urlpatterns = [
    path('all/', BookListView.as_view(), name="all_books"),
]
