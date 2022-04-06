from django.urls import path
from author.views import AuthorListView, AuthorDetailView
from . import views

urlpatterns = [
    path('all/', AuthorListView.as_view(), name="all_authors"),
    path('<int:pk>/', AuthorDetailView.as_view(), name="author_detail"),
    path('new/', views.create_author, name="create_author"),
]
