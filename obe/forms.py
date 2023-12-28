from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields =  ['id', 'full_name', 'email', 'phone_num', 
                  'reservation_date', 'reservation_slot', 'people', 'comment']