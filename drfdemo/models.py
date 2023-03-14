from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,verbose_name="姓名")
    sex = models.BooleanField(default=1,verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    class_null = models.CharField(null=True,max_length=5,verbose_name="班级编号")
    description = models.TextField(null=True,max_length=100,verbose_name="个性签名")

    class Meta:
        db_table="tb_student"
        # verbose_name = "学生"
        # verbose_name_plural = verbose_name

class Book(models.Model):
    title = models.CharField(max_length=32,verbose_name="书籍名称")
    price = models.IntegerField(verbose_name="价格")
    pub_data = models.DateField(verbose_name="出版日期")

class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
