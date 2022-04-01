from django.views import generic

from order.models import Order


class OrderListView(generic.ListView):

    model = Order
    context_object_name = "orders"
    template_name = 'order/list.html'

class SortedOrderView(generic.ListView):

    template_name = 'order/sorted.html'
    context_object_name = 'orders'

    def get_queryset(self):

        param = self.request.GET.get('param', '?')
        sorting = self.request.GET.get('sorting')
        queryset = Order.objects.order_by(param)

        if sorting == 'asc':
            return queryset
        return queryset.reverse()