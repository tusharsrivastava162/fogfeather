from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=False)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50, null=False)


class Employee(User):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
