from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    emailid=models.EmailField()
    city=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
