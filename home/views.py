from django.shortcuts import render
from .models import Department, Doctor
from .forms import BookingForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def doctors_view(request):
    doctors_list = Doctor.objects.all() 
    return render(request, 'doctors.html', {'doc': doctors_list})

def contact(request):
    return render(request, 'contact.html')

def department_view(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'dept': departments})
