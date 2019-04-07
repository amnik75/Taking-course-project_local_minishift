from login.models import Student
from login.api.serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GetInfo(APIView):
    
    def post(self,request,format=None):
        s = Student.objects.filter(student_number = request.data['student_number']).first()
        if s == None:
           return Response('The student is not founded')
        serializer = StudentSerializer(s)
        return Response(serializer.data)

class UpInfo(APIView):
    
    def post(self,request,format=None):
        s = Student.objects.filter(student_number = request.data['student_number']).first()
        if s == None:
           return Response('The student is not founded')
        s.average = request.data['average']
        s.save()
        return Response('Info updated successfully')


class Signup(APIView):

    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, format= None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("You are signed up successfully", status=status.HTTP_200_OK)
        elif isRepeating(request.data) :
            return Response("The student number or id number is used by other user!", status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_200_OK)

class Login(APIView):

    def post(self, request, format=None):
        if isExist(request.data):
            return Response("You are loged in successfully", status=status.HTTP_200_OK)
        else:
            return Response("The student number or id number is not correct!", status=status.HTTP_200_OK)

def isExist(data):
    if "student_number" in data and "id_number" in data:
        student_number = data["student_number"]
        id_number = data["id_number"]
        students = Student.objects.all()
        for student in students:
            if student.student_number == student_number and student.id_number == id_number:
                return True
    return False

def isRepeating(data):
    if "student_number" in data and "id_number" in data:
        student_number = data["student_number"]
        id_number = data["id_number"]
        students = Student.objects.all()
        for student in students:
            if student.student_number == student_number or student.id_number == id_number:
                return True
    return False
