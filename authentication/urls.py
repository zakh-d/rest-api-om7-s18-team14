from django.urls import path
from rest_framework.routers import SimpleRouter

from authentication.views import CustomUserCreationView, CustomUserUpdateView, CustomUserAPIView, CustomUserOrdersAPIView

router = SimpleRouter()
router.register('', CustomUserAPIView)
router.register(r'(?P<user_id>\d+)/order', CustomUserOrdersAPIView, basename="Order")

urlpatterns = [
    path('create/', CustomUserCreationView.as_view(), name="create_user"),
    path('update/<int:pk>/', CustomUserUpdateView.as_view(), name="update_user"),
]
