from django import forms
from django.forms import DateInput
from .models import Booking

class DateTimeInput(DateInput):
    input_type = 'datetime-local'

class BookingForm(forms.Form):
    start_time = forms.DateTimeField(widget=DateTimeInput())
    end_time = forms.DateTimeField(widget=DateTimeInput())
    purpose = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("End time must be after start time.")
        
        return cleaned_data
