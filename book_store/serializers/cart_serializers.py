from rest_framework import serializers

from book_store.models import CartItem,  Book
from book_store.serializers.book_serializers import BookSerializer


class CartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'book', 'quantity')
        depth = 1


class CartItemCreateSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)

    def create(self, validated_data):
        # Extract book_id and quantity from validated_data
        book_id = validated_data['book_id']
        quantity = validated_data['quantity']

        # Assuming you have a user-related cart (OneToOneField)
        cart = self.context['request'].user.cart

        # Retrieve the book instance
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            raise serializers.ValidationError(f"Book with ID {book_id} not found.")

        if book.stock_quantity < quantity:
            raise serializers.ValidationError({"details": f"There are only {book.stock_quantity} items of **{book.title}**"
                                                          f" in the store"})
        # Check if the book is already in the cart, and if so, update the quantity
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity += (quantity -1)

        cart_item.save()

        return cart_item
