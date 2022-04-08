from rest_framework import serializers
from author.models import Author


class CreateAuthorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Author
        fields = ('id', 'name', 'surname', 'patronymic')


class UpdateAuthorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Author
        fields = ('id', 'name', 'surname', 'patronymic')
        exclude_fields = ('id',)


class RetrieveAuthorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Author
        fields = ('id', 'name', 'surname', 'patronymic')
