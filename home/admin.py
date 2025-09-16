from django.contrib import admin
from .models import Department, Doctor, Booking

admin.site.register(Department)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'patient_phone', 'patient_email', 'doctor_name', 'date')

admin.site.register(Booking, BookingAdmin)
