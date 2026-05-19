from django.db import models


class signupm(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile_No=models.CharField(max_length=15)
    password=models.CharField(max_length=255)


class loginp(models.Model):
    email=models.EmailField()
    password=models.CharField()

# Create your models here.
