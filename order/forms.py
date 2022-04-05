from django import forms
from order.models import Order


class OrderCreationForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('user', 'book', 'plated_end_at')
        
    def __init__(self, *args, **kwargs):
        super(OrderCreationForm, self).__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = lambda obj: f'{obj.first_name} {obj.last_name}'
        self.fields['book'].label_from_instance = lambda obj: obj.name
