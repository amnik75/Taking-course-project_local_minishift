from rest_framework import serializers
from login.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_number', 'firstName', 'lastName')
