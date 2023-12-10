from django.forms import ModelForm
from .models import Booking, Contact
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model  = Booking
        fields = '__all__'
        
        
# class ContactForm(forms.ModelForm):
#     class Mate:
#         model = Contact
#         fields = '__all__'