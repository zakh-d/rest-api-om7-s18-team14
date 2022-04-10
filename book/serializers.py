from rest_framework import serializers
from book.models import Book
from author.serializers import AuthorListSerializer


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'count')


class BookCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'count', 'authors')


class BookRetrieveSerializer(serializers.ModelSerializer):

    authors = AuthorListSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'count', 'authors')