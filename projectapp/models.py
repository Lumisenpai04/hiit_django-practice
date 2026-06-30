from django.db import models

# Create your models here.

"""class Employees:
    def __init__(self, full_name,department,status):
        self.full_name = full_name
        self.department = department
        self.status = status
"""


class Employees(models.Model):
    full_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    staus = models.CharField(max_length=50)
    year = models.IntegerField()