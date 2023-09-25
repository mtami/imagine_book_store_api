from rest_framework import generics
from book_store.models.book_model import Book
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from book_store.serializers.book_serializers import BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'genre']


class BookDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
