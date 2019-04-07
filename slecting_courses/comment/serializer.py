from rest_framework import serializers
from comment.models import Comment
from login.api.serializers2 import StudentSerializer
class CommentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id','content','student','time')