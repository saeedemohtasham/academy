from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import requests
# Create your views here.
clas_list=[
    {'id':1,'name':'پایتون','time_in':'14:30','time_out':'15','description':'استاد: آقای احمدی، روزهای برگزاری :شنبه و دوشنبه'},
    {'id':2,'name':'جنگو','time_in':'17:30','time_out':'19','description':'استاد: آقای رسولی، روزهای برگزاری :دوشنبه و چهارشنبه',},
    {'id':3,'name':'icdl','time_in':'16:30','time_out':'18','description':'استاد: آقای نیازی، روزهای برگزاری :سه شنبه و پنج شنبه'},
    {'id':4,'name':'هوش مصنوعی','time_in':'16','time_out':'17:30','description':'استاد: خانم امیری، روزهای برگزاری :شنبه و چهارشنبه',}
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
#exercise 8
def clas_detail(request,name):
    f_list=[]
    for item in clas_list:
        if name in item['name'] or name in item['description']:
            f_list.append(item)
    context={"filter":f_list}
    return render (request,'list/list.html',context=context)
    
def search2(request):
    f_list=[]
    search=request.GET.get('search')
    
    for item in clas_list:
        if search in item['name'] or search in item['description']:
            f_list.append(item)
            context={"filter":f_list}
            return render (request,'list/list2.html',context=context)
    else:
        return render(request,'list/notfound.html')