from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        mode = Book
        fields = ("title", "subtitle", "author", "isbn")