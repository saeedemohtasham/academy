from . import views
from django.urls import path
urlpatterns = [
    path('list-class/',views.show_list),
]
