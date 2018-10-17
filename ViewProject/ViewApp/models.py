from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    bookname=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    price=models.FloatField()
    publisher=models.CharField(max_length=30)

    def __str__(self):
        return self.bookname

    def get_absolute_url(self):
        return reverse("detail",kwargs={'pk':self.pk})
