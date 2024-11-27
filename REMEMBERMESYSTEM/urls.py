from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('stureg/',views.stureg,name='stureg'),
    path('faculty/',views.faculty,name='faculty'),
    path('studentlogin/',views.studentlogin,name='studentlogin'),
    path('studentlog/',views.studentlog,name='studentlog'),
    path('studentwelcome/',views.studentwelcome,name='studentwelcome'),
    path('welcome/',views.welcome,name='welcome'),
    path('facultylogin/',views.facultylogin,name='facultylogin'),
    path('facultylog/',views.facultylog,name='facultylog'),
    path('views/',views.views,name='views'),
    path('eventview/',views.eventview,name='eventview'),
    path('update/<str:pk>',views.update,name='update'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('reports/',views.reports,name='reports'),
    path('inbox/',views.inbox,name='inbox'),
    path('birthday/',views.birthday,name='birthday'),
    path('file/',views.file,name='file'),
]