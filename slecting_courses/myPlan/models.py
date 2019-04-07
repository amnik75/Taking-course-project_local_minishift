from django.db import models
from django.apps import apps
from login.models import Student
from chooseClass.models import Class

# Create your models here.

class Plan(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='stplan', null=False, blank=False, default=None)
    classes = models.ManyToManyField(Class, blank=True)




# Create your models here.
