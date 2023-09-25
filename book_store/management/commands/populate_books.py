import os
import json
from django.core.management.base import BaseCommand
from book_store.models.book_model import Book


class Command(BaseCommand):
    help = 'Populate the Book model with data from a JSON file'

    def handle(self, *args, **kwargs):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        json_file = os.path.join(parent_directory, 'books.json')

        try:
            with open(json_file, 'r') as file:
                books_data = json.load(file)

            for book_data in books_data:
                Book.objects.create(**book_data)

            self.stdout.write(self.style.SUCCESS('Successfully populated the Book model from the JSON file.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('JSON file not found. Please provide the correct file path.'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format in the file.'))
