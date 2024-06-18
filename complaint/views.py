from django.shortcuts import render

from complaint.models import Complaint

# Create your views here.


#def feedback(request):
 #   return render(request, 'Feedback.html')

def complaint(request):
    return render(request,'complaint.html')

def history(request):
    my_user = request.user
      #to get aa complaints stored in database table 'complaint' 

    return render(request, 'history.html')