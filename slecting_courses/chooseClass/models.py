from django.db import models
# Create your models here.

class Course(models.Model):
    courseId = models.CharField(primary_key=True,max_length=10)
    courseName = models.CharField(max_length=20,blank=False,null=False)
    units = models.CharField(max_length=2,blank=False,null=False)
    havePreCourse = models.CharField(max_length=1, blank=False, null=False)
    havePeriCourse = models.CharField(max_length=1, blank=False, null=False)
    preCourse = models.ManyToManyField("self",blank=True,symmetrical=False, related_name='PreCourse')
    periCourse = models.ManyToManyField("self",blank=True,symmetrical=False, related_name='PeriCourse')



class Teacher(models.Model):
    teacherId = models.CharField(primary_key=True,max_length=3)
    teacherName = models.CharField(max_length=20,blank=False,null=False)

class Class(models.Model):
    classId = models.CharField(primary_key=True,max_length=2)
    examTime = models.CharField(blank=False,null=False,max_length=10)
    examDay = models.CharField(blank=True,null=False,max_length=10)
    courseTime = models.CharField(blank=False,null=False,max_length=10)
    courseDay = models.CharField(blank=False,null=False,max_length=10)
    capacity = models.CharField(blank=False,null=False,max_length=3)
    semester = models.CharField(blank=False,null=False,max_length=7)
    registered = models.IntegerField(blank=False,null=True,default=0)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=False,blank=False,default=None)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=False,blank=False,default=None)
    registered = models.IntegerField(blank=False,null=True,default=0)
    
