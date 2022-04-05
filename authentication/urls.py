from django.urls import path

from authentication.views import CustomUserCreationView

urlpatterns = [
    path('create', CustomUserCreationView.as_view(), name="create_user"),

]
