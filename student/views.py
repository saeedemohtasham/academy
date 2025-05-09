from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student
from dore.models import Course
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework import viewsets
from .serializer import StudentsSerializer
# Create your views here.
def show_list(request):
    return HttpResponse('hello')

def register(request):
    name=request.GET.get('name')
    family=request.GET.get('family')
    age=request.GET.get('age')
    mobile=request.GET.get('mobile')
    email=request.GET.get('email')
    password=request.GET.get('password')
    student=Student(name=name,family=family,age=age,mobile=mobile,email=email,password=password)
    student.save()
    return HttpResponse("done!")

def course_register(request):
    stu_id=request.GET.get('student_id')
    s1=Student.objects.get(pk=stu_id)
    # print(student.name)
    cou_id=request.GET.get('course_id')
    co=Course.objects.get(pk=cou_id)
    # print(co.name)
    list=co.students.all()
    # print(list[0].name)
    for item in list:

        if item.id != stu_id:
            s1.courses.add(co)
            return HttpResponse("ok!")
    else:
       return HttpResponse("کاربر تکراری است")
def show_list(request,course_id):
    course=Course.objects.get(pk=course_id)
    list=course.student.all()
    for item in list:
        return HttpResponse(item.name,item.family)

def detail(request,course_id):
    course=Course.objects.get(pk=course_id)
    context={"filter":course}
    return render (request,'html/detail.html',context=context)
class StudentsViewSets(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    def get_serializer(self, *args, **kwargs):
        if self.request.method=='GET':
            if self.kwargs.get('pk'):
                return StudentsSerializer(*args,**kwargs)
            else:
                return StudentsSerializer(*args,**kwargs,fields=['id','name','family'])
        elif self.request.method=='POST':
            return StudentsSerializer(*args,**kwargs)
        elif self.request.method=='PUT':
            return StudentsSerializer(*args,**kwargs) 
        elif self.request.method=='DELETE':
            return StudentsSerializer(*args,**kwargs)
        else:
            return StudentsSerializer(*args,**kwargs)