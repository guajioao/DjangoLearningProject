from abc import ABC

from django.shortcuts import render,HttpResponse
from django.views import View
from rest_framework.views import APIView
from drfdemo.models import Student
from rest_framework.response import Response
from drfdemo.serializers import StudentSerializer,StuModelSerializer


class LoginView(View):

    def dispatch(self, request, *args, **kwargs):
        #执行分发之前的公共逻辑操作
        print("dispatch")
        #引用父类方法
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self,request):

        return HttpResponse("LoginView GET...")

    def post(self,request):

        return HttpResponse("LoginView POST...")

# Create your views here.

# class StuModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['name','sex','age']

# class StudentView(APIView):
#
#     # def dispatch(self, request, *args, **kwargs):
#     #     #执行分发之前的公共逻辑操作
#     #     print("dispatch")
#     #     #引用父类方法
#     #     ret = super().dispatch(request, *args, **kwargs)
#     #     return ret
#
#     def get(self,request):
#         students_all = Student.objects.all()
#         for stu in students_all:
#             print(stu.id,stu.name,stu.sex,stu.age,stu.description)
#         print(students_all)
#         # many=True,表示有多个
#         serializers = StudentSerializer(instance=students_all,many=True)
#         return Response(serializers.data)
#
#     def post(self,request):
#         #json直接转dict
#         data_dict = request.data
#         serializers = StudentSerializer(data=data_dict)
#
#         try:
#             serializers.is_valid(raise_exception=True)
#             print(type(serializers.validated_data))
#             stu = Student.objects.create(**serializers.validated_data)
#             ser = StudentSerializer(instance=stu,many=False)
#             return Response(ser.data)
#         except Exception as e:
#             print("e",e)
#             return Response(serializers.errors)

class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(pk=id)
        serializers = StudentSerializer(instance=student,many=False)
        print(id)
        return Response(serializers.data)

    def delete(self,request,id):
        Student.objects.get(pk=id).delete()
        return Response("删除成功")

    def put(self,request,id):
        # json直接转dict
        data_dict = request.data
        serializers = StudentSerializer(data=data_dict)
        try:
            serializers.is_valid(raise_exception=True)

            print("validated_data",serializers.validated_data)
            stu = Student.objects.filter(pk=id).update(**serializers.validated_data)
            # ser = StudentSerializer(instance=stu, many=False)
            return Response(stu)
        except Exception as e:
            print("e", e)
            return Response(serializers.errors)

# class StuModelView(APIView):
#     def get(self,request):
#         students = Student.objects.all()
#         ss = StuModelSerializer(instance=students,many=True)
#         return Response(ss.data)
#
#     def post(self,request):
#         serializers = StuModelSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response()

#################################################混合类，封装所有get,post,put
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView


class StudentView(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StuModelSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class StuModelView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StuModelSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk=pk)

    def delete(self,request,pk):
        return self.destroy(request,pk=pk)

    def put(self,request,pk):
        return self.update(request,pk=pk)