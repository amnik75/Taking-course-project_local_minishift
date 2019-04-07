from chooseClass.models import Class,Course,Teacher
from chooseClass.serializers import ClassSerializer,CourseSerializer,TeacherSerializer
from login.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GetClasses(APIView):

    def get(self, request, format= None):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes,many=True)
        return Response(serializer.data)

class GetPreCourse(APIView):

    def get(self,request,pk,format = None):
        course = Course.objects.filter(courseId = pk).first()
        serializer = CourseSerializer(course.preCourse,many = True)
        return Response(serializer.data)

class GetPeriCourse(APIView):

    def get(self,request,pk,format = None):
        course = Course.objects.filter(courseId = pk).first()
        serializer = CourseSerializer(course.periCourse,many = True)
        return Response(serializer.data)

class Register(APIView):

    def post(self,request,format = None):
        c = Class.objects.filter(classId = request.POST["classId"]).first()
        if c == None:
            return Response("The class is not found",status=status.HTTP_200_OK)
        student = Student.objects.filter(student_number = request.POST['student_number']).first()
        if student == None:
            return Response("The student is not found", status=status.HTTP_200_OK)
        temp = student.classes.filter(classId = c.classId).first()
        if temp == None:
          student.classes.add(c)
       	  c.registered = c.registered + 1
          c.save()
          return Response("Student " + request.POST['student_number'] + " is registered successfully" , status=status.HTTP_200_OK)
        return Response("Student " + request.POST['student_number'] + " is registered recently" , status=status.HTTP_200_OK)
