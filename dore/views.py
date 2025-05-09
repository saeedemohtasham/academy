from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework import viewsets
from .models import Course
from .serializer import CouresesSerializer
from student.models import Student


# Create your views here.
@api_view(['get'])
def show_list(request:Request):
    course=Course.objects.all()
    course_serializer=CouresesSerializer(course,many=True,fields=['name','teacher_name'])
    return Response({'courses':course_serializer.data},status=status.HTTP_200_OK)


def student_list(request:Request,id:int):
    # course_id=request.GET.get('course_id')
    cou=Course.objects.filter(id=id)
    Course.students.filter(cou)


@api_view(['post'])
def create_course(request:Request):
    #  return Response({"name": "gholi"},status=status.HTTP_200_OK)
    serializer=CouresesSerializer(data=request.data)
    if serializer.is_valid():
        if Course.objects.all().filter(name=request.data["name"]).exists():
            return Response({'errors':{"name":"نام تکراری است"}},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({"course":serializer.data},status=status.HTTP_200_OK)
    else:
        return Response ({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['put'])
def update_course(request:Request,id:int):
    cou=Course.objects.filter(id=id).first()
    if cou:
        co_serializer=CouresesSerializer(data=request.data)
        if co_serializer.is_valid():
            co_serializer.save()
            
            return Response({'course':co_serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"course":co_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response ({"course": None}, status=status.HTTP_404_NOT_FOUND)

class ListCreatApiView(APIView):
    def get(self,request:Request):
        course=Course.objects.all()
        course_serializer=CouresesSerializer(course,many=True,fields=['name','teacher_name'])
        return Response({'courses':course_serializer.data},status=status.HTTP_200_OK)
    def post(self,request:Request):
        serializer=CouresesSerializer(data=request.data)
        if serializer.is_valid():
            if Course.objects.all().filter(name=request.data['name']).exists():
                return Response({'errors':{"name":"نام تکراری است"}},status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response({"course": serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'errors':serializer.errors},status=status.HTTP_404_NOT_FOUND)
class GetUpdateDeleteApiView(APIView):
    def get_course(self,id):
        return Course.objects.filter(id=id).first()
    def get(self,request:Request,id:int):
        co=self.get_course(id=id)
        if co:
            course_serializer=CouresesSerializer(co)
            return Response({'course':course_serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'course':None},status=status.HTTP_404_NOT_FOUND)
    def put(self,request:Request,id:int):
        co=self.get_course(id=id)
        if co:
            course_serializer=CouresesSerializer(co,data=request.data,fields=['name','teacher_name'])
            if course_serializer.is_valid():
                course_serializer.save()
                course_serializer=CouresesSerializer(co)
                return Response({"course":course_serializer.data},status=status.HTTP_200_OK)
            else:
                return Response({'course':course_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request:Request,id:int):
        co=self.get_course(id=id)
        if co:
            co.delete()
            return Response({"'massage":"deleted"})

class ListCreatMixinApiView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Course.objects.all()
    def get_serializer(self, *args, **kwargs):
        if self.request.method=='GET':
            kwargs['fields']=['name','teacher_name']
            return CouresesSerializer(*args,**kwargs)
        else:
            return CouresesSerializer(*args,**kwargs)
    def get(self,request:Request):
        return self.list(request)
    def post(self,request:Request):
        return self.create(request)
    
class GetUpdateDeleteMixinApiView(mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=Course.objects.all()
    def get_serializer(self, *args, **kwargs):
        if self.request.method=='GET':
            kwargs['fields']=['name','teacher_name']
            return CouresesSerializer(*args,**kwargs)
        else:
            return CouresesSerializer(*args,**kwargs)
    def get(self,request:Request,pk:int):
        return self.retrieve(request,pk)
    
    def put(self,request:Request,pk:int):
        return self.update(request,pk)
    def delete(self,request:Request,pk:int):
        return self.destroy(request,pk)

class CoursesViewSets(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    def get_serializer(self, *args, **kwargs):
        if self.request.method=='GET':
            if self.kwargs.get('pk'):
                return CouresesSerializer(*args,**kwargs)
            else:
                return CouresesSerializer(*args,**kwargs,fields=['id','name'])
        elif self.request.method=='POST':
            return CouresesSerializer(*args,**kwargs)
        elif self.request.method=='PUT':
            return CouresesSerializer(*args,**kwargs) 
        elif self.request.method=='DELETE':
            return CouresesSerializer(*args,**kwargs)
        else:
            return CouresesSerializer(*args,**kwargs)