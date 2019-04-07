from rest_framework import serializers
from myPlan.models import Plan
from chooseClass.serializers import ClassSerializer

class PlanSerializer(serializers.ModelSerializer):
    classes = ClassSerializer(read_only = True,many = True)
    class Meta:
        model = Plan
        fields = ('id','classes')
