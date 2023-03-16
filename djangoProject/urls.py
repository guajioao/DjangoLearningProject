"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path

# from app01 import views
from drfdemo import views
from drfdemo.views import LoginView,StudentView,StuModelView

from rest_framework import routers
router = routers.DefaultRouter()
router.register('drfdemo/publish', views.PublishView)
router.register('drfdemo/author', views.AuthorDetailView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('orm/',views.orm),
    # path('login/',LoginView.as_view()),
    # path('drfdemo/student/',StudentView.as_view()),
    # re_path('drfdemo/student/(\d+)/',views.StudentDetailView.as_view()),
    # path('drfdemo/student/<int:id>/',StuModelView.as_view()),
    # path('drfdemo/publish/',views.PublishView.as_view()),
    # re_path('drfdemo/publish/(?P<pk>\d+)/',views.PublishDetailView.as_view()),
    # path('drfdemo/author/',views.AuthorView.as_view({
    #     "get":"list",
    #     "post":"create"
    # })),
    # re_path('drfdemo/author/(?P<pk>\d+)/',views.AuthorDetailView.as_view({
    #     "get": "retrieve",
    #     "post": "create",
    #     "put": "update",
    #     "delete": "destroy"
    # })),


]
urlpatterns += router.urls


