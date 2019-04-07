from comment.models import Comment
from login.models import Student
from chooseClass.models import Teacher,Course
from comment.serializer import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GetComment(APIView):

    def post(self,request,format=None):
        teacherId = request.POST['teacherId']
        courseId = request.POST['courseId']
        serializer = CommentSerializer(Comment.objects.filter(teacher_id=teacherId,course_id=courseId),many=True)
        return Response(serializer.data)

class SetComment(APIView):

    def post(self,request,format=None):
        teacherId = request.POST['teacherId']
        courseId = request.POST['courseId']
        studentNumber = request.POST['studentNumber']
        content = request.POST['content']
        t = Teacher.objects.filter(teacherId=teacherId).first()
        course = Course.objects.filter(courseId=courseId).first()
        student = Student.objects.filter(student_number=studentNumber).first()
        if t != None and course != None and student != None:
            c = Comment(teacher=t,course=course,student=student,content=content)
            c.save()
            return Response("The comment is saved successfuly")
        else:
            return Response("The teacher or student or course is not found")