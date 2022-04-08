from rest_framework import serializers
from book.models import Book


class CreateBookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ('id', 'name', 'description', 'count', 'authors')


class UpdateBookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ('id', 'name', 'description', 'count', 'authors')
        exclude_fields = ('id',)


class RetrieveBookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ('id', 'name', 'description', 'count', 'authors')