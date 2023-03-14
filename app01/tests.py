from django.test import TestCase

# Create your tests here.

class A(object):
    name = "a0"
    def __init__(self,name,age):
        self.name = name
        self.age = age

a = A("a1",13)
b = A("a2",5)