from django.urls import path
from book.views import BookListView, BookDetailView, UnorderedBookView, FilterBooksView

urlpatterns = [
    path('all/', BookListView.as_view(), name="all_books"),
    path('available/', UnorderedBookView.as_view(), name="unordered_books"),
    path('filter/', FilterBooksView.as_view(), name="filter_books"),
    path('<int:pk>/', BookDetailView.as_view(), name="book_detail"),
]
