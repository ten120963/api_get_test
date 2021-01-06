from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('add_course.html', views.add_course, name="add_course"),
    path('delete/<course_id>', views.delete, name="delete"),
    path('delete_course.html>', views.delete_course, name="delete_course"),
]
