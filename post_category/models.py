from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    emp_relation = models.ManyToManyField(Employee)


    def __str__(self):
        return self.name


