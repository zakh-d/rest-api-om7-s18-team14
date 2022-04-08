from django.urls import path
from rest_framework.routers import SimpleRouter

from order.views import OrderCreationView, OrderDebtorsView, OrderUserBooksView, SortedOrderView, OrderListView, \
    OrderUpdateView, OrdersAPIView

router = SimpleRouter()
router.register('', OrdersAPIView)

urlpatterns = [
    path('all/', OrderListView.as_view(), name="all_orders"),
    path('sorted/', SortedOrderView.as_view(), name="sorted_orders"),
    path('user_books/<int:pk>/', OrderUserBooksView.as_view(), name="user_books"),
    path('debtors/', OrderDebtorsView.as_view(), name="debtors"),
    path('create/', OrderCreationView.as_view(), name="create_order"),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name="update_order"),
]
