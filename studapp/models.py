from django.db import models

# Create your models here.


class Student(models.Model):
    Id = models.IntegerField(primary_key=True)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Date_of_birth = models.DateField()
    Email = models.TextField(null=False)
    Class_level = models.IntegerField(null=False)
    Parent_name = models.CharField(max_length=100)
    Phone_number = models.IntegerField(unique=True)
    DateAdded = models.DateField(auto_created=True)
    DateUpdated = models.DateField(auto_now=True)
    Year_joined = models.IntegerField()
