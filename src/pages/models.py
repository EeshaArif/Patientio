""" from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length = 150, null = True, blank = True)
    last_name = models.CharField(max_length = 150, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    phone = models.CharField(max_length = 20, null = True, blank = True)
    age = models.IntegerField(null = True, blank = True)
    sex = models.CharField(max_length = 15, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    image = models.FileField(upload_to = 'images/', default = '')
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
        return '%s %s' %(self.first_name, self.last_name)

class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)
    date = models.DateField('date selected')
    time = models.TimeField('time selected')
    doctor = models.IntegerField(null = True, blank = True)
    disease_option = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):
        return '%s' %(self.date)

class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)
    first_name = models.CharField(max_length = 150,null = True, blank = True)
    last_name = models.CharField(max_length = 150,null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    phone = models.CharField(max_length = 20,null = True, blank = True)
    age = models.IntegerField(null = True, blank = True)
    sex = models.CharField(max_length = 15,null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    image = models.FileField(upload_to = 'images/', default = '')
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
        return '%s %s' %(self.first_name, self.last_name)

class LabDoc(models.Model):
    first_name = models.CharField(max_length = 150, null = True, blank = True)
    last_name = models.CharField(max_length = 150, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    phone = models.CharField(max_length = 20, null = True, blank = True)
    age = models.IntegerField(null = True, blank = True)
    sex = models.CharField(max_length = 15, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    image = models.FileField(upload_to = 'images/', default = '')
    designation = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField()

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Receptionist(models.Model):
    first_name = models.CharField(max_length = 150, null = True, blank = True)
    last_name = models.CharField(max_length = 150, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    phone = models.CharField(max_length = 20, null = True, blank = True)
    age = models.IntegerField(null = True, blank = True)
    sex = models.CharField(max_length = 15, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    image = models.FileField(upload_to = 'images/', default = '')
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField()

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Nurse(models.Model):
    first_name = models.CharField(max_length = 150, null = True, blank = True)
    last_name = models.CharField(max_length = 150, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    phone = models.CharField(max_length = 20, null = True, blank = True)
    age = models.IntegerField(null = True, blank = True)
    sex = models.CharField(max_length = 15, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    image = models.FileField(upload_to = 'images/', default = '')
    designation = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField()

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

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
        return '%s' %(self.about_data)

class Service(models.Model):
    service_title = models.CharField(max_length = 50)
    service_summary = models.CharField(max_length = 150)
    text = models.TextField()
    image = models.FileField(upload_to = 'images/', default = '')
    icon = models.FileField(upload_to = 'images/', default = '')

    def __str__(self):
        return self.service_title

class Report(models.Model):
    test_name = models.CharField(max_length = 30)
    date = models.DateField('date of report generation')
    result_summary = models.CharField(max_length = 200)
    investigations =models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)
    lab_doctor = models.ForeignKey(LabDoc, on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    test_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.test_name
"""

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.utils import timezone
import datetime
# Create your models here.

GENDER_CHOICES = (('m', 'Male'),('f', 'Female'),('o', 'Other'))
DUTY_DAY_CHOICES = (('Mon', 'Monday'),('Tues','Tuesday'),('Wed', 'Wednesday'),('Thurs', 'Thursday'),('Fri', 'Friday'),('Sat', 'Saturday'),('Sun', 'Sunday'))

class Doctor(models.Model):
    first_name = models.CharField(max_length = 150, default = '')
    last_name = models.CharField(max_length = 150, default = '')
    address = models.CharField(max_length = 200, default = '')
    phone = models.CharField(max_length = 20, default = '')
    age = models.IntegerField(default = 0,validators=[MinValueValidator(0)])
    sex = models.CharField(max_length = 1, default = '', choices = GENDER_CHOICES)
    email = models.EmailField(default = '')
    image = models.FileField(upload_to = 'images/', default = '')
    designation = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField(validators=[MinValueValidator(0)])
    professional_statement_text = models.TextField()
    education =models.TextField()
    payment_statement = models.TextField()
    start_duty_day = models.CharField(max_length = 9, choices = DUTY_DAY_CHOICES)
    end_duty_day = models.CharField(max_length = 9, choices = DUTY_DAY_CHOICES)
    start_time = models.TimeField('start time')
    end_time = models.TimeField('end time')

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)
    date = models.DateField('date selected')
    time = models.TimeField('time selected')
    doctor = models.IntegerField(default = 0)
    disease_option = models.CharField(max_length = 50, default = '')

    def __str__(self):
        return '%s' %(self.date)

class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)
    first_name = models.CharField(max_length = 150, default = '')
    last_name = models.CharField(max_length = 150, default = '')
    address = models.CharField(max_length = 200, default = '')
    phone = models.CharField(max_length = 20, default = '')
    age = models.IntegerField(default = 0,validators=[MinValueValidator(0)])
    sex = models.CharField(max_length = 1, default = '', choices = GENDER_CHOICES)
    email = models.EmailField(default = '')
    image = models.FileField(upload_to = 'images/', default = '')
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
        return '%s %s' %(self.first_name, self.last_name)

class LabDoc(models.Model):
    first_name = models.CharField(max_length = 150, default = '')
    last_name = models.CharField(max_length = 150, default = '')
    address = models.CharField(max_length = 200, default = '')
    phone = models.CharField(max_length = 20, default = '')
    age = models.IntegerField(default = 0,validators=[MinValueValidator(0)])
    sex = models.CharField(max_length = 1, default = '', choices = GENDER_CHOICES)
    email = models.EmailField(default = '')
    image = models.FileField(upload_to = 'images/', default = '')
    designation = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Receptionist(models.Model):
    first_name = models.CharField(max_length = 150, default = '')
    last_name = models.CharField(max_length = 150, default = '')
    address = models.CharField(max_length = 200, default = '')
    phone = models.CharField(max_length = 20, default = '')
    age = models.IntegerField(default = 0,validators=[MinValueValidator(0)])
    sex = models.CharField(max_length = 1, default = '', choices = GENDER_CHOICES)
    email = models.EmailField(default = '')
    image = models.FileField(upload_to = 'images/', default = '')
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Nurse(models.Model):
    first_name = models.CharField(max_length = 150, default = '')
    last_name = models.CharField(max_length = 150, default = '')
    address = models.CharField(max_length = 200, default = '')
    phone = models.CharField(max_length = 20, default = '')
    age = models.IntegerField(default = 0,validators=[MinValueValidator(0)])
    sex = models.CharField(max_length = 1, default = '', choices = GENDER_CHOICES)
    email = models.EmailField(default = '')
    image = models.FileField(upload_to = 'images/', default = '')
    designation = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    experience = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

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
    price = models.DecimalField(max_digits=20, decimal_places=2,validators=[MinValueValidator(0)])
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='price')

    def __str__(self):
        return '%s %s' %(self.disease_name, self.price)

class About(models.Model):
    about_data = models.TextField()

    def __str__(self):
        return '%s' %("About")

class Service(models.Model):
    service_title = models.CharField(max_length = 50)
    service_summary = models.CharField(max_length = 150)
    text = models.TextField()
    image = models.FileField(upload_to = 'images/', default = '')
    icon = models.FileField(upload_to = 'images/', default = '')

    def __str__(self):
        return self.service_title

class Report(models.Model):
    test_name = models.CharField(max_length = 30)
    date = models.DateField('date of report generation')
    result_summary = models.CharField(max_length = 200)
    investigations =models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)
    lab_doctor = models.ForeignKey(LabDoc, on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    test_price = models.DecimalField(max_digits=20, decimal_places=2,validators=[MinValueValidator(0)])

    def __str__(self):
        return self.test_name
