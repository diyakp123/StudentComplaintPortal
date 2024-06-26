from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name="user"),
    path('FacultySolvedComplaints',views.FacultySolvedComplaints,name="FacultySolvedComplaints"),
    path('FacultyUnsolvedComplaints',views.FacultyUnsolvedComplaints,name="FacultyUnsolvedComplaints"),
    path('FacultyInprogressComplaints',views.FacultyInprogressComplaints,name="FacultyInprogressComplaints"),
    path('ComplaintDetail', views.ComplaintDetail, name="ComplaintDetail")
]
