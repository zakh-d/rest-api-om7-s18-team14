from django.urls import path

from authentication.views import CustomUserCreationView, CustomUserUpdateView

urlpatterns = [
    path('create/', CustomUserCreationView.as_view(), name="create_user"),
    path('update/<int:pk>/', CustomUserUpdateView.as_view(), name="update_user"),
]
