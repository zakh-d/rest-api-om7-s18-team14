from django.urls import path
from order.views import *

urlpatterns = [
    path('all/', OrderListView.as_view(), name="all_orders"),
    path('sort_id', SortedIDOrderView.as_view(), name="sort_id_orders"),
    path('sort_user_id', SortedUserIdOrderView.as_view(), name="sort_user_id_orders"),
    path('sort_book_id', SortedBookIdOrderView.as_view(), name="sort_book_id_orders"),
    path('sort_created', SortedCreatedOrderView.as_view(), name="sort_created_orders"),
    path('sort_ended', SortedEndOrderView.as_view(), name="sort_end_orders"),
    path('sort_plated', SortedPlatedOrderView.as_view(), name="sort_plated_orders"),
]
