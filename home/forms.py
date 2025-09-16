from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }
        labels = {
            'patient_name': "Patient Name : ",
            'patient_phone': "Patient Phone : ",
            'patient_email': "Patient Email : ",
            'doctor_name': "Doctor Name : ",
            'date': "Booking Date : ",
        }
