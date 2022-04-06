from django.urls import reverse_lazy
from django.views import generic
from django.db.models import F
from order.forms import OrderCreationForm, OrderUpdateForm
from order.models import Order
from authentication.models import CustomUser
from datetime import datetime
import pytz


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


class OrderUserBooksView(generic.DetailView):  # Використовуємо DetailView, бо він сам дістає юзера по pk
    model = CustomUser
    context_object_name = 'user'
    template_name = 'order/user_books.html'

    def get_context_data(self, **kwargs):
        context = super(OrderUserBooksView, self).get_context_data(**kwargs)
        user = self.get_object()
        books = set(map(lambda order: order.book, user.orders.all()))
        context['books'] = books

        return context


class OrderDebtorsView(generic.ListView):
    context_object_name = 'users'
    template_name = 'order/debtors.html'

    def get_queryset(self):
        late_returners = Order.objects.filter(end_at__gte=F('plated_end_at')).values_list("user_id", flat=True)
        debtors = Order.objects.filter(end_at=None).values_list("user_id", flat=True).filter(plated_end_at__gte=datetime.now(tz=pytz.UTC))

        return CustomUser.objects.all().filter(pk__in=late_returners|debtors).order_by("pk")


class OrderCreationView(generic.CreateView):

    model = Order
    form_class = OrderCreationForm
    template_name = 'order/create.html'
    success_url = reverse_lazy('all_orders')


class OrderUpdateView(generic.UpdateView):

    model = Order
    form_class = OrderUpdateForm
    template_name = 'order/update.html'
    success_url = reverse_lazy('all_orders')
