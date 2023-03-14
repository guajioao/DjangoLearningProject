from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=18)

class Department(models.Model):
    title = models.CharField(max_length=16)

#新建数据库 insert into ****
# Department.objects.create(title="销售部")
# UserInfo.objects.create(name="yy",password="123456",age=20)