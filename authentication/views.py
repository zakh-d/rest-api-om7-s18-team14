from django.views import generic

from authentication.forms import CustomUserCreationForm, CustomUserUpdateForm
from authentication.models import CustomUser


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
