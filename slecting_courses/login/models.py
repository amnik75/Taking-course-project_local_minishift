from chooseClass.models import Class
from django.db import models

# Create your models here.


class Student(models.Model):
    student_number = models.CharField(max_length=254,primary_key=True,blank = False,null = False)
    id_number = models.CharField(max_length = 10,blank = False,null = False,unique=True)
    average = models.IntegerField(blank = False,null = False)
    entery_year = models.CharField(max_length = 4, blank=False, null=False)
    firstName = models.CharField(max_length = 254,blank=True, null=True)
    lastName = models.CharField(max_length = 254,blank=True, null=True)
    major = models.CharField(max_length = 254,blank=True,null=True)
    classes = models.ManyToManyField(Class,blank=True)
    regPlan = models.OneToOneField('myPlan.Plan',on_delete=models.CASCADE,null = True,blank=True,default = None,related_name='rplan')


