from django.views import generic
from django.db.models import F
from order.models import Order
from authentication.models import CustomUser



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

        for o in queryset:
            print(o.book)

        if sorting == 'asc':
            return queryset

        return queryset.reverse()

    # def get_context_data(self, **kwargs):
    #     context = super(SortedOrderView, self).get_context_data(**kwargs)
    #     books = list(map(lambda order: order.book, user.orders.all()))
    #     context['books'] = books
    #
    #     return context


class OrderUserBooksView(generic.DetailView):  # Використовуємо DetailView, бо він сам дістає юзера по pk
    model = CustomUser
    context_object_name = 'user'
    template_name = 'order/user_books.html'

    def get_context_data(self, **kwargs):
        context = super(OrderUserBooksView, self).get_context_data(**kwargs)
        user = self.get_object()
        books = list(map(lambda order: order.book, user.orders.all()))
        context['books'] = books
        
        return context


class OrderDebtorsView(generic.ListView):
    context_object_name = 'users'
    template_name = 'order/debtors.html'

    def get_queryset(self):
        late_returners = Order.objects.filter(end_at__gte=F('plated_end_at')).values_list("user_id", flat=True)
        debtors = Order.objects.filter(end_at=None).values_list("user_id", flat=True)

        return CustomUser.objects.all().filter(pk__in=late_returners|debtors)
