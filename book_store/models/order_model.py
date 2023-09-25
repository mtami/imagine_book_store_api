from django.db import models
from django.contrib.auth.models import User  # If using Django's built-in User model
from model_utils.models import TimeStampedModel, SoftDeletableModel

from book_store.models.book_model import Book


class Order(TimeStampedModel, SoftDeletableModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book, through='OrderItem')

    def __str__(self):
        return f'Order #{self.id} by {self.user.username}'


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.book.title} in Order #{self.order.id}'
