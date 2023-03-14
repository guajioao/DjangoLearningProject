from rest_framework import serializers
from drfdemo.models import Student,Publish,Author

class StudentSerializer(serializers.Serializer):
    # source指model里的变量名，names指url里的名字
    names = serializers.CharField(source="name",max_length=5)
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    class_null = serializers.CharField(allow_null=True)
    description = serializers.CharField(allow_null=True,max_length=100)

    def create(self, validated_data):
        new_student = Student.objects.create(validated_data)
        return new_student

    def update(self, instance, validated_data):
        Student.objects.filter(pk=instance.pk).update(**validated_data)
        updated_student = Student.objects.get(pk=id)
        return updated_student


class StuModelSerializer(serializers.ModelSerializer):
    names = serializers.CharField(source="name")
    class Meta:
        model = Student #自动根据model中Student表创建
        #fields和exclude只能选一个用
        # fields = ['name', 'sex', 'age']
        # fields = "__all__"
        exclude = ['name']# 自己写了names之后，记得把name排除掉

class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


