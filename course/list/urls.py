from . import views
from django.urls import path
urlpatterns = [
    path('list-class/',views.show_list ),
    path('course-list',views.course_list,name="list"),
    path('search/<name>', views.search)
]
