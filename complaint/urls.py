from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name="user"),
     path('feedback', views.feedback, name="feedback"),
     path('complaint', views.complaint, name="complaint"),
     path('StudentComplaintHistory', views.StudentComplaintHistory, name="StudentComplaintHistory"),
     path('StudentSolvedComplaints',views.StudentSolvedComplaints,name="StudentSolvedComplaints"),
     path('StudentUnsolvedComplaints',views.StudentUnsolvedComplaints,name="StudentUnsolvedComplaints"),
     path('StudentInprogressComplaints',views.StudentInprogressComplaints,name="StudentInprogressComplaints"),
     path('thankyou', views.thankyou, name="thankyou"),
     path('ComplaintDetail', views.ComplaintDetail, name="ComplaintDetail")
]
