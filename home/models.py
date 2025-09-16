from django.db import models

class Department(models.Model):
    dep_name = models.CharField(max_length=50)
    dep_description = models.TextField()  

    def __str__(self):
        return self.dep_name


class Doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=100)
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return f"Dr {self.doc_name} - ({self.doc_spec})"


class Booking(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_phone = models.IntegerField()
    patient_email = models.CharField(max_length=50)
    doctor_name = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.patient_name
