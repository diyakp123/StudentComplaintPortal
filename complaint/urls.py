from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name="user"),
    path('feedback/<int:id>', views.feedback, name="feedback"),
    path('feedbacksubmit', views.feedbacksubmit, name="feedbacksubmit"),

    path('complaint', views.complaint, name="complaint"),
    path('StudentComplaintHistory', views.StudentComplaintHistory, name="StudentComplaintHistory"),
    path('StudentSolvedComplaints',views.StudentSolvedComplaints,name="StudentSolvedComplaints"),
    path('StudentUnsolvedComplaints',views.StudentUnsolvedComplaints,name="StudentUnsolvedComplaints"),
    path('StudentInprogressComplaints',views.StudentInprogressComplaints,name="StudentInprogressComplaints"),
    path('thankyou', views.thankyou, name="thankyou"),
    path('StudentComplaintDetail/<int:id>', views.StudentComplaintDetail, name="StudentComplaintDetail"),
    path('studentlogout',views.studentlogout,name='studentlogout'),
    path('FilterData', views.FilterData,name="FilterData")

]
