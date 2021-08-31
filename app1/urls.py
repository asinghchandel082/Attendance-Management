from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submitdata', views.submit, name='submit'),
    path('showstudents', views.getStudents, name='getStudents'),
    path('add_attendance/<int:rollno>/', views.add_attendance, name='addattendance'),
    path('show_attendance/<int:rollno>/', views.show_attendance, name='showattendance'),
]