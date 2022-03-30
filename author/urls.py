from django.urls import path
from author.views import AuthorListView, AuthorDetailView

urlpatterns = [
    path('all/', AuthorListView.as_view(), name="all_authors"),
    path('<int:pk>/', AuthorDetailView.as_view(), name="author_detail"),
]
