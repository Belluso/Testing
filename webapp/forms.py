from .models import *
from django import forms


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment;
        fields = '__all__';
        # widgets  = {
        #     'ApartmentNumber' : forms.NumberInput(attrs={'class': 'input input-primary bg-base-100', 
        #                                                  'placeholder': 'Apartment Number'}),
        #     'NumBedrooms' : forms.NumberInput(attrs={'class': 'input input-primary bg-base-100', 
        #                                              'placeholder': 'Number of Bedrooms'}),
        #     'NumBathrooms' : forms.NumberInput(attrs={'class': 'input input-primary bg-base-100', 
        #                                              'placeholder': 'Number of Bathroom'}),
            
        #     'RentAmount' : forms.NumberInput(attrs={'class': 'input input-primary bg-base-100', 
        #                                              'placeholder': 'Rent Amount'}),
        # }