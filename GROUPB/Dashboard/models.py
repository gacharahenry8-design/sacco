from django.db import models
import datetime

# Create your models here.
class Student:
    pass

from django.db import models

class Student(models.Model):
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField()


    def __str__(self):
        return self.name


class Student2(models.Model):
   name = models.CharField(max_length=20)
   exam_code = models.IntegerField()
   date = models.DateField(auto_now_add=True)

   def __str__(self):
       return self.name

