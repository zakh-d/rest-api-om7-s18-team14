from rest_framework import serializers

from authentication.serializers import RetrieveUserSerializer
from book.serializers import BookSerializer
from order.models import Order


class RetrieveOrderSerializer(serializers.ModelSerializer):

    user = RetrieveUserSerializer()
    book = BookSerializer()

    class Meta:

        model = Order
        fields = ('id', 'user', 'book', 'created_at', 'plated_end_at', 'end_at')


class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order
        fields = ('user', 'book', 'plated_end_at')


class UpdateOrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order
        fields = ('plated_end_at', )
