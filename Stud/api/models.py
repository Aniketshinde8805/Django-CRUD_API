from django.db import models
from datetime import datetime
# Create your models here.

class Student(models.Model):
    g_options=(
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    )
    name = models.CharField(max_length=100)
    rollno=models.IntegerField(unique=True)
    bdate=models.DateField(auto_now_add=True,auto_now=False,blank=True)
    blood=models.CharField(max_length=20)
    gender=models.CharField(max_length=30,choices=g_options)

    def __str__(self):
        return self.name
    
    