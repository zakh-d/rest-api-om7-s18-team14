from django.views import generic

from order.models import Order
from authentication.models import CustomUser
from book.models import Book
from django.shortcuts import render
import logging



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


class OrderDebtorsView(generic.ListView):

    model = Order
    template_name = "order/debtors.html"

    def get_context_data(self, **kwargs):
        context = super(OrderDebtorsView, self).get_context_data(**kwargs)
        orders_1 = Order.objects.filter(end_at=None).values_list('user_id', flat=True)
        context['users'] = CustomUser.objects.all()
        context['books'] = Order.objects.all()
        return context


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
