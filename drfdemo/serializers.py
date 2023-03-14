from rest_framework import serializers
from drfdemo.models import Student

class StudentSerializer(serializers.Serializer):
    # source指model里的变量名，names指url里的名字
    names = serializers.CharField(source="name",max_length=5)
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    class_null = serializers.CharField(allow_null=True)
    description = serializers.CharField(allow_null=True,max_length=100)

class StuModelSerializer(serializers.ModelSerializer):
    names = serializers.CharField(source="name",max_length=5)
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    class_null = serializers.CharField(allow_null=True)
    description = serializers.CharField(allow_null=True,max_length=100)
    class Meta:
        model = Student
        fields = ['name', 'sex', 'age']
