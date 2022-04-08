from django.urls import path
from rest_framework.routers import SimpleRouter

from authentication.views import CustomUserCreationView, CustomUserUpdateView, CustomUserAPIView

router = SimpleRouter()
router.register('', CustomUserAPIView)

urlpatterns = [
    path('create/', CustomUserCreationView.as_view(), name="create_user"),
    path('update/<int:pk>/', CustomUserUpdateView.as_view(), name="update_user"),
]
