from rest_framework import serializers

from book_store.models import  OrderItem
from book_store.serializers.book_serializers import BookReadSerializer


class OrderItemBookSerializer(serializers.ModelSerializer):
    book = BookReadSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'book', "quantity")
        depth = 1

