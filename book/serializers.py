from rest_framework import serializers
from book.models import Book
from author.serializers import AuthorSerializer


class RetrieveBookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'count', 'authors')


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'count')
