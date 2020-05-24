from django.db import models

# Create your models here.
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    RollNo = models.IntegerField()
    Name = models.CharField(max_length=20)
    Status = models.IntegerField()
    Date = models.CharField(max_length=20)