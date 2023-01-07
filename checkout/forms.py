from django import forms
from .models import order
from userprofile.models import userDetails


class orderForm():
    class Meta:
        model = order
        fields = ('full_name', 'email','phone_number',
                'country','postcode','town',
                'city','street_name','house_number')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country':'country',
            'postcode': 'Post Code',
            'town': 'Town',
            'city':'city',
            'street_name': 'Street name',
            'house_number':'House number',
        }
        
        self.fields['full_name'].widgets.attrs['autofocus'] = True4567
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label.widget.attrs['class'] = 'form-label'