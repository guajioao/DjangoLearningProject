from abc import ABC

from django.shortcuts import render,HttpResponse
from django.views import View
from rest_framework.views import APIView
from drfdemo.models import Student,Publish,Author
from rest_framework.response import Response
from drfdemo.serializers import StudentSerializer,StuModelSerializer,PublishSerializer,AuthorSerializer


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
###############基于APIView的接口实现
class StudentView(APIView):
    def get(self,request):
        students_all = Student.objects.all()
        for stu in students_all:
            print(stu.id,stu.name,stu.sex,stu.age,stu.description)
        print(students_all)
        # many=True,表示有多个
        serializers = StudentSerializer(instance=students_all,many=True)
        return Response(serializers.data)

    def post(self,request):
        #json直接转dict
        data_dict = request.data
        serializers = StudentSerializer(data=data_dict)

        try:
            serializers.is_valid(raise_exception=True)
            print(type(serializers.validated_data))
            stu = Student.objects.create(**serializers.validated_data)
            ser = StudentSerializer(instance=stu,many=False)
            return Response(ser.data)
        except Exception as e:
            print("e",e)
            return Response(serializers.errors)

class StudentDetailView(APIView):
    def get(self,request,id):
        print(id)
        student = Student.objects.get(pk=id)
        serializers = StudentSerializer(instance=student,many=False)
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

class StuModelView(APIView):
    def get(self,request):
        students = Student.objects.all()
        ss = StuModelSerializer(instance=students,many=True)
        return Response(ss.data)

    def post(self,request):
        serializers = StuModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response()

##############################基于GenericAPIView的接口实现
from rest_framework.generics import GenericAPIView

class PublishView(GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer

    def get(self,request):
        serializer = self.get_serializer(instance=self.get_object(),many=True)
        return Response(serializer.data)

    def post(self,request):
        print("data:",request.data)
        serializer = self.get_serializer(instance=self.get_object())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PublishDetailView(GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer
    # lookup_field = 'name'

    def get(self,request,pk):
        # publish_list = self.get_queryset().filter(pk=pk)
        serializer = self.get_serializer(instance=self.get_object(),many=False)
        # serializer = self.get_serializer(instance=publish_list,many=True)
        return Response(serializer.data)

    def put(self,request,pk):
        print("data:",request.data)
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):
        self.get_object().delete()
        return Response("删除")


############################## 基于Mixin混合类的接口实现 ###############################
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
class AuthorView(GenericAPIView, ListModelMixin, CreateModelMixin,):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)



class AuthorDetailView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # lookup_field = 'name'

    def get(self,request,pk):
        return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request)

    def delete(self,request,pk):
        return self.destroy(request)
