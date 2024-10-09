from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_joining = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 

class PunchRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    punch_in_time = models.DateTimeField(null=True, blank=True)
    punch_out_time = models.DateTimeField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

