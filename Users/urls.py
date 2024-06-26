from django.urls import path
from . import views

urlpatterns = [
     path('',views.home, name="home"),
     path('home',views.home, name="home"),
     path('dashboard',views.dashboard, name="dashboard"),
     path('roles',views.roles, name="roles"),
     path('studentlogin',views.studentlogin, name="studentlogin"),
     path('facultylogin',views.facultylogin, name="facultylogin"),
     path('facultydashboard',views.Facultydashboard, name="facultydashboard"),
     path('registration',views.registration, name="registration"),
     path('contactus',views.contactus,name="contactus"),
     path('studentlogout',views.studentlogout,name='studentlogout'),
     path('facultylogout',views.facultylogout,name='facultylogout'),

]
