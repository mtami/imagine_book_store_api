from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response

from book_store.models import Order, CartItem, OrderItem
from book_store.serializers.order_serializers import  OrderItemBookSerializer


class OrderHistoryList(generics.ListAPIView):
    serializer_class = OrderItemBookSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created']

    def get_queryset(self):
        # Retrieve orders associated with the authenticated user
        return OrderItem.objects.filter(order__user=self.request.user)


class PlaceOrderView(generics.CreateAPIView):
    serializer_class = None
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user = request.user

        # Retrieve the user's cart items
        cart_items = CartItem.objects.filter(cart__user=user)
        if not cart_items.exists():
            raise serializers.ValidationError({"details": "There are no items in the user's shopping cart."})

        # Create a new order with the cart items
        order = Order.objects.create(user=user)
        for cart_item in cart_items:
            OrderItem.objects.create(order=order, book=cart_item.book, quantity=cart_item.quantity)
            book = cart_item.book
            book.stock_quantity -= cart_item.quantity
            book.save()

        # Delete all the cart items for the user
        cart_items.delete()

        return Response({"message": "Order placed successfully."}, status=status.HTTP_201_CREATED)
