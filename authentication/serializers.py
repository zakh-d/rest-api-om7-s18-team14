from rest_framework import serializers
from authentication.models import CustomUser, ROLE_CHOICES


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = ('id', 'email', 'first_name', 'middle_name', 'last_name', 'password')


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = ('email', 'first_name', 'middle_name', 'last_name')


class RetrieveUserSerializer(serializers.ModelSerializer):

    role = serializers.ChoiceField(choices=ROLE_CHOICES, source='get_role_display')

    class Meta:

        model = CustomUser
        exclude = ('last_login', 'is_active', 'password')
