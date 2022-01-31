from django.db import models


# Create your models here.

class Employee(models.Model):
     name=models.CharField(max_length=20)
     emp_id=models.IntegerField(max_length=10)
     phone_num=models.IntegerField(max_length=10)
     salary=models.IntegerField(max_length=10)


class News1(models.Model):
    date = models.DateTimeField()
    image=models.ImageField(upload_to='static/images')
    news=models.CharField(max_length=10000)
     
