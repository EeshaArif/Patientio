from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
import datetime
from django.utils import timezone
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    address = models.CharField(max_length = 200, null = True, blank = True)
    phone = models.CharField(max_length = 20)
    age = models.IntegerField()
    sex = models.CharField(max_length = 15)
    email = models.EmailField(null = True, blank = True)
    image = models.ImageField(null = True, blank = True)

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Doctor(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    designation = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField()
    professional_statement_text = models.TextField()
    education =models.TextField()
    payment_statement = models.TextField()
    start_duty_day = models.CharField(max_length = 9)
    end_duty_day = models.CharField(max_length = 9)
    start_time = models.TimeField('start time')
    end_time = models.TimeField('end time')

    def __str__(self):
        return '%s %s' %(self.person.first_name, self.person.last_name)

class Patient(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' %(self.person.first_name, self.person.last_name)

class History(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='p_history')
    occupation = models.CharField(max_length = 100, null = True, blank = True)
    presenting_complaint = models.TextField(null = True, blank = True)
    presenting_complaint_detail = models.TextField(null = True, blank = True)
    past_medical_history = models.TextField(null = True, blank = True)
    past_surgical_history =models.TextField(null = True, blank = True)
    past_drug_history = models.TextField(null = True, blank = True)
    drug_allergy = models.TextField(null = True, blank = True)
    vaccination_history = models.TextField(null = True, blank = True)
    personal_history = models.TextField(null = True, blank = True)
    economic_status = models.TextField(null = True, blank = True)

    def __str__(self):
        return '%s %s' %(self.patient.person.first_name, self.patient.person.last_name)

class LabDoc(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    designation = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField()

    def __str__(self):
        return '%s %s' %(self.person.first_name, self.person.last_name)

class Receptionist(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField()

    def __str__(self):
        return '%s %s' %(self.person.first_name, self.person.last_name)

class Nurse(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    designation = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField()

    def __str__(self):
        return '%s %s' %(self.person.first_name, self.person.last_name)

class Curriculum(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='curriculum')
    major_subject = models.CharField(max_length = 200)

    def __str__(self):
        return self.major_subject

class Specialization(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='specialization')
    specialization = models.CharField(max_length = 200)

    def __str__(self):
        return self.specialization

class Payment(models.Model):
    disease_name = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='price')

    def __str__(self):
        return '%s %s' %(self.disease_name, self.price)

class About(models.Model):
    about_data = models.TextField()

    def __str__(self):
        return '%s' %("About")

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name='appointment', null = True, blank = True)
    date = models.DateField('date selected')
    time = models.TimeField('time selected')

    def __str__(self):
        return '%s' %(self.date)

class Service(models.Model):
    service_title = models.CharField(max_length = 50)
    service_summary = models.CharField(max_length = 150)
    text = models.TextField()
    image = models.ImageField(null = True, blank = True)
    icon = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.service_title

class Report(models.Model):
    test_name = models.CharField(max_length = 30)
    date = models.DateField('date of report generation')
    result_summary = models.CharField(max_length = 200)
    investigations =models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    lab_doctor = models.ForeignKey(LabDoc, on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    test_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return '%s %s %s' %(self.test_name, self.patient.person.first_name, self.patient.person.last_name)
