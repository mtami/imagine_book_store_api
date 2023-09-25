from rest_framework import serializers

from book_store.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('is_removed',)


class BookReadSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()
    genre = serializers.CharField()
    price = serializers.DecimalField(max_digits=4, decimal_places=2)