from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
routher=DefaultRouter()
routher.register('',views.StudentsViewSets)
urlpatterns = [
    path('list-class/',views.show_list ),
    path('register/',views.register),
    path('co-register/',views.course_register),
    path('list/<int:course_id>',views.show_list,name="list"),
    path('detail/<int:course_id>',views.detail),
    path('viewset/',include(routher.urls)),
    
    
    
]
