# views.py
from rest_framework import  status, generics, serializers
from rest_framework.response import Response
from book_store.models import  CartItem
from book_store.serializers.cart_serializers import CartItemSerializer, CartItemCreateSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import permissions


class CartListShopView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)


class CartItemCreateView(CreateAPIView):
    serializer_class = CartItemCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        cart_item = super().get_object()

        # Check if the cart item belongs to the authenticated user
        if cart_item.cart.user != self.request.user:
            raise serializers.ValidationError("You don't have permission to delete this cart item.")

        return cart_item

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
