from django.db import models

# Create your models here.
class Course(models.Model):
    name= models.CharField(max_length=50)
    teacher_name= models.CharField(max_length=50)
    #1:در حال ثبت نام    
    #2:در حال برگزاری
    #3:اتمام یافته
    #4:لغو شده
    status=models.IntegerField(default=1)
    is_deleted=models.BooleanField(default=False)
    class Meta():
        db_table="courses1"


