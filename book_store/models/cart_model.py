from django.db import models
from django.contrib.auth.models import User  # If using Django's built-in User model
from model_utils.models import TimeStampedModel, SoftDeletableModel

from book_store.models.book_model import Book


class Cart(TimeStampedModel, SoftDeletableModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.email}"


class CartItem(TimeStampedModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.book.title} in Cart"



