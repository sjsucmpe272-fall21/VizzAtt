from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('searchattendence/', views.searchAttendence, name='searchattendence'),
    path('account/', views.facultyProfile, name='account'),
    path('updateFaculty/', views.updateFaculty, name='updateFaculty'),
    path('updateStudentRedirect/', views.updateStudentRedirect, name='updateStudentRedirect'),
    path('updateStudent/', views.updateStudent, name='updateStudent'),
    path('attendance/', views.takeAttendence, name='attendence'),
]