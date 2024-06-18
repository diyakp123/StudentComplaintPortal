from django.urls import path
from . import views

urlpatterns = [
     path('',views.home, name="home"),
     path('home',views.home, name="home"),
     path('dashboard',views.dashboard, name="dashboard"),
     path('login',views.login, name="login"),
     path('registration',views.registration, name="registration"),
     path('contactus',views.contactus,name="contactus")
]
