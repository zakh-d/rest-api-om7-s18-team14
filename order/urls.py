from django.urls import path
from order.views import *

urlpatterns = [
    path('all/', OrderListView.as_view(), name="all_orders"),
    path('sorted/', SortedOrderView.as_view(), name="sorted_orders"),
    path('user_books/<int:pk>', OrderUserBooksView.as_view(), name="user_books"),
    path('debtors/', OrderDebtorsView.as_view(), name="debtors"),
]
