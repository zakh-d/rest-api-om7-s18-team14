from django.urls import path
from book.views import BookListView, BookDetailView

urlpatterns = [
    path('all/', BookListView.as_view(), name="all_books"),
    path('<int:pk>/', BookDetailView.as_view(), name="book_detail"),
]
