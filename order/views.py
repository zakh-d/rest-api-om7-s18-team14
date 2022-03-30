from django.views import generic

from order.models import Order


class OrderListView(generic.ListView):

    model = Order
    context_object_name = "orders"
    template_name = 'order/list.html'

class SortedIDOrderView(generic.ListView):

    context_object_name = 'orders'
    template_name = 'order/list.html'

    def get_queryset(self):

        return Order.objects.order_by('id')

class SortedUserIdOrderView(generic.ListView):

    context_object_name = 'orders'
    template_name = 'order/list.html'

    def get_queryset(self):

        return Order.objects.order_by('user_id')

class SortedBookIdOrderView(generic.ListView):

    context_object_name = 'orders'
    template_name = 'order/list.html'

    def get_queryset(self):

        return Order.objects.order_by('book_id')


class SortedCreatedOrderView(generic.ListView):

    context_object_name = 'orders'
    template_name = 'order/list.html'

    def get_queryset(self):

        return Order.objects.order_by('created_at')

class SortedEndOrderView(generic.ListView):

    context_object_name = 'orders'
    template_name = 'order/list.html'

    def get_queryset(self):

        return Order.objects.order_by('end_at')

class SortedPlatedOrderView(generic.ListView):

    context_object_name = 'orders'
    template_name = 'order/list.html'

    def get_queryset(self):

        return Order.objects.order_by('plated_end_at')