from rest_framework import serializers
from chooseClass.models import Class,Course,Teacher


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('courseId', 'courseName', 'units','havePreCourse','havePeriCourse')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('teacherId', 'teacherName')

class ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Class
        fields = ('classId', 'examTime', 'examDay', 'courseTime', 'courseDay', 'capacity','registered','semester','teacher','course')
