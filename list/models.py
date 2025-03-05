from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    age=models.IntegerField()
    mobile=models.CharField(max_length=12,null=True)
    email=models.CharField(max_length=50,null=True)
    is_active=models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)
    password=models.CharField(max_length=50)
    class Meta():
        db_table="users"
class Course(models.Model):
    name= models.CharField(max_length=50)
    teacher_name= models.CharField(max_length=50)
    #1:در حال ثبت نام    
    #2:در حال برگزاری
    #3:اتمام یافته
    #4:لغو شده
    status=models.SmallIntegerField(default=1)
    is_deleted=models.BooleanField(default=False)
    class Meta():
        db_table="courses"