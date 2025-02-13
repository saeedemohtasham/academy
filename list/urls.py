from . import views
from django.urls import path
urlpatterns = [
    path('list-class/',views.show_list ),
    path('course-list',views.course_list,name="list"),
    path('filter/<name>', views.filter),
    path('detail/<name>',views.detail, name="detail"),
    path('detail2',views.detail2),
    path('search/<name>',views.search),
    path('clas-detail/<name>',views.clas_detail, name="clas-detail"),
    path('search2/',views.search2),
]
