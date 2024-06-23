from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name="user"),
     path('feedback', views.feedback, name="feedback"),
     path('complaint', views.complaint, name="complaint"),
     path('FacultyComplaint', views.FacultyComplaint, name="FacultyComplaint"),
     path('thankyou', views.thankyou, name="thankyou"),
]
