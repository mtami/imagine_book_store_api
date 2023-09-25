from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Book(TimeStampedModel, SoftDeletableModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()

    # You can add more fields like ISBN, publication_date, etc. here

    def __str__(self):
        return self.title
