from django.urls import path
from book.views import BookListView, BookDetailView, UnorderedBookView, FilterBooksView, SortedBookView, create_book, edit_book, BookAPIView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', BookAPIView)

urlpatterns = [
    path('all/', BookListView.as_view(), name="all_books"),
    path('available/', UnorderedBookView.as_view(), name="unordered_books"),
    path('filter/', FilterBooksView.as_view(), name="filter_books"),
    path('sorted/', SortedBookView.as_view(), name="sorted_books"),
    path('<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('new/', create_book, name='create_book'),
    path('<int:pk>/edit/', edit_book, name='edit_book'),
]
