from . import views
from django.urls import path,include
from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('',views.CoursesViewSets)
urlpatterns = [
    path('list-class/',views.show_list ),
    path('list-student/<int:id>',views.student_list ),
    path('create',views.create_course ),
    path('update/<int:id>',views.update_course ),
    path('class/course',views.ListCreatApiView.as_view()),
    path('class/course/<int:id>',views.GetUpdateDeleteApiView.as_view()),
    path('class/mixincourse/',views.ListCreatMixinApiView.as_view()),
    path('class/mixincourse/<int:pk>',views.GetUpdateDeleteMixinApiView.as_view()),
    path('viewset/', include(router.urls))
]
