from django.db import models
from login.models import Student
from chooseClass.models import Teacher,Course
# Create your models here.
class Comment(models.Model):
    content = models.TextField(blank=True,null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    time = models.DateField(blank=True,null=True,auto_now=True)