from rest_framework import serializers
from author.models import Author
from book.models import Book


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'count')


class AuthorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')


class AuthorRetrieveSerializer(serializers.ModelSerializer):
    books = BookListSerializer(many=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'surname', 'patronymic', 'books')


class AuthorCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic', 'books')



