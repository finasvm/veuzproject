from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    department = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    additional_info = models.JSONField(blank=True, null=True) 

    def __str__(self):
        return self.name

