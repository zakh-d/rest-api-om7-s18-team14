from django.views import generic
from rest_framework import viewsets
from authentication.forms import CustomUserCreationForm, CustomUserUpdateForm
from authentication.models import CustomUser
from authentication.serializers import CreateUserSerializer, UpdateUserSerializer, RetrieveUserSerializer


class CustomUserCreationView(generic.CreateView):

    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'authentication/create_update.html'
    success_url = '/book/all'
    extra_context = {'title': 'Create User'}


class CustomUserUpdateView(generic.UpdateView):

    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'authentication/create_update.html'
    success_url = '/book/all'
    extra_context = {'title': 'Update User'}


class CustomUserAPIView(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()

    def get_serializer_class(self):

        if self.action in ('list', 'retrieve'):
            return RetrieveUserSerializer
        if self.action == 'create':
            return CreateUserSerializer
        return UpdateUserSerializer
