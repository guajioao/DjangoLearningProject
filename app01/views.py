from django.shortcuts import render,HttpResponse
from django.views import View
from app01.models import Department,UserInfo

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def userAdd(request):
    #
    return render(request,"user.html")

def tpl(request):
    name = 1
    roles = ['1','2','3']
    return render(request,"tpl.html",{"n1": name, "n2":roles})

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

def orm(request):
    #新建
    # Department.objects.create(title="d1")
    # UserInfo.objects.create(name="yy",age=20,password="123456")

    #删除
    # Department.objects.filter(title="销售部").delete()
    # UserInfo.objects.filter(name="yy").delete()

    #获取
    #data_list = [行，行，行] QuerySet类型
    # data_list = UserInfo.objects.all()
    # data_list = UserInfo.objects.filter(name="yy")
    # for obj in data_list:
    #     print(obj.id,obj.name,obj.password,obj.age)
    # obj = UserInfo.objects.filter(name="yy").first()
    # print(obj.id, obj.name, obj.password, obj.age)

    #更新数据
    # UserInfo.objects.all().update(password="123654")
    UserInfo.objects.filter(name="yy").update(age=22)

    return HttpResponse("成功")