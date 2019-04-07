from chooseClass.models import Class
from myPlan.models import Plan
from login.models import Student
from myPlan.serializers import PlanSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class GetPlans(APIView):

    def post(self, request, format= None):
        plan = Plan.objects.filter(student__student_number = request.POST['student_number'])
        if plan == None:
            return Response("The student or plan is not found")
        serializer = PlanSerializer(plan,many = True)
        return Response(serializer.data)

class CreatePlan(APIView):

    def post(self, request, format= None):
        student = Student.objects.filter(student_number=request.POST['student_number']).first()
        if student == None:
            return Response("The student not found")
        p = Plan(student = student)
        p.save()
        classes = request.POST["classes_id"]
        for id in classes.split(","):
            c = Class.objects.filter(classId = id).first()
            if c == None:
                return Response("Class with id " + id + " not found")
            p.classes.add(c)
        return Response("The plan is created for student successfully")

class Register(APIView):

    def post(self,request,format = None):
        student = Student.objects.filter(student_number=request.POST['student_number']).first()
        if student == None:
            return Response("The student is not found")
        if student.regPlan != None:
            return Response("The student was registered recently")
        p = Plan.objects.filter(id = request.POST["id"]).first()
        if p == None:
            return Response("The plan is not found")
        if p.student.student_number != student.student_number:
            return Response("This plan is not chosen by this student")
        for c in p.classes.all():
            c.registered = c.registered + 1
            c.save()
            student.classes.add(c)
        student.regPlan = p
        student.save()
        return Response("Student " + request.POST['student_number'] + " is registered in classes successfully")

class UpdateRegister(APIView):

    def post(self,request,format = None):
        student = Student.objects.filter(student_number=request.POST['student_number']).first()
        if student == None:
            return Response("The student is not found")
        p = Plan.objects.filter(id = request.POST["id"]).first()
        if p == None:
            return Response("The plan is not found")
        if student.regPlan == None:
            return Response("The student was not registered before")
        if student.regPlan.id == p.id:
            return Response("The registeration is not changed")
        for c in student.regPlan.classes.all():
            c.registered = c.registered - 1
            c.save()
            student.classes.remove(c)
        for c in p.classes.all():
            c.registered = c.registered + 1
            c.save()
            student.classes.add(c)
        student.regPlan = p
        student.save()
        return Response("The registeration is updated successfully")
