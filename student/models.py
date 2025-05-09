from django.db import models
from django.urls import reverse
from dore.models import Course

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    age=models.IntegerField()
    mobile=models.CharField(max_length=12,null=True)
    email=models.CharField(max_length=50,null=True)
    is_active=models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)
    password=models.CharField(max_length=50)
    courses=models.ManyToManyField(Course,related_name="students")
    class Meta():
        db_table="students"
    # def get_detail(self):
    #     return reverse('user-detail',args=[self.id])

    