from django.db import models

# Create your models here.
class Student(models.Model):
    FirstName = models.CharField(max_length=20, blank=False, null=False)
    LastName = models.CharField(max_length=15, blank=False, null=False)
    RollNo = models.IntegerField(primary_key=True)
    Email = models.EmailField(max_length=40, blank=False, null=False)
    RegistrationDate = models.CharField(max_length=40, blank=False, null=False)
    Class = models.CharField(max_length=40, blank=False, null=True)
    Gender = models.CharField(max_length=10, blank=False, null=False)
    MobileNo = models.IntegerField()
    ParentsName = models.CharField(max_length=40, blank=False, null=False)
    ParentMobileNo = models.IntegerField()
    BirthDate = models.CharField(max_length=20)
    BloodGroup = models.CharField(max_length=40, blank=False, null=False)
    Address = models.CharField(max_length=40, blank=False, null=False)