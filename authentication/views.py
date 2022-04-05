from django.views import generic

from authentication.forms import CustomUserCreationForm
from authentication.models import CustomUser


class CustomUserCreationView(generic.CreateView):

    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'authentication/create.html'
    success_url = '/book/all'
