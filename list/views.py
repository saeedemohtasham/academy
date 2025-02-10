from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import requests
# Create your views here.
clas_list=[
    {'id':1,'name':'python','time_in':'14:30','time_out':'15'},
    {'id':2,'name':'django','time_in':'17:30','time_out':'19'},
    {'id':3,'name':'icdl','time_in':'16:30','time_out':'18'},
    {'id':4,'name':'hoosh','time_in':'16','time_out':'17:30'}
]
    
def show_list(request):
    data=""
    for item in clas_list:
        #url= reverse('academy detail',args=[item['id']])
        data= data + f"id:{item['id']},name:{item['name']},time_in:{item['time_in']},time_out:{item['time_out']}"+"<br>"
    return HttpResponse(data)

def course_list(request):
    context={'filter':clas_list}
    return render (request,'list/list2.html',context=context)
def detail(request,name):
    return HttpResponse(f"class list:{name}")

def filter(request,name):
    data=""
    for item in clas_list:
        if name in item['name']:
            url=reverse('detail',args=[item['name']])
            data= data +f"<a href='{url}' target='_blank'> {item['name']}</a>" + "<br>"
    return HttpResponse(data)
def detail2 (request):
    f_list=[]
    id=request.GET.get('id')
    id=int(id)
    for item in clas_list:
        if id==item['id']:
            f_list.append(item)
            context={"filter":f_list}
            return render (request,'list/list2.html',context=context)
    else:
        return render(request,'list/eror.html')

def search(request,name):
    filter_list=[]
    for item in clas_list:
        if name in item['name']:
            filter_list.append(item)
    context={'filter':filter_list}
    return render(request,'list/list2.html',context=context)