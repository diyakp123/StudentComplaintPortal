from django.shortcuts import redirect, render

from Users.models import User
from Users.views import Facultydashboard
from complaint.models import Complaint

# Create your views here.


def user(request):
    return Facultydashboard(request)

def FacultySolvedComplaints(request):
   # facultyemail = request.session['facultyemail']
    #facultypwd = request.session['facultypwd']
    if 'facultyemail' in request.session:
        #mail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            #pwd = request.session['facultypwd']
            try:
        #result = FacultyUser.objects.get(email=uemail, password=password)
                result2 = Complaint.objects.filter(status_id=1).values()
                print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2} )
            except User.DoesNotExist as e:
                print("sde")
                return render(request, 'dashboard')

    return redirect('home')


def FacultyUnsolvedComplaints(request):
   # facultyemail = request.session['facultyemail']
    #facultypwd = request.session['facultypwd']
    if 'facultyemail' in request.session:
        #mail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            #pwd = request.session['facultypwd']
            try:
        #result = FacultyUser.objects.get(email=uemail, password=password)
                result2 = Complaint.objects.filter(status_id=2).values()
                print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2} )
            except User.DoesNotExist as e:
                print("sde")
                return render(request, 'dashboard')

    return redirect('home')


def FacultyInprogressComplaints(request):
   # facultyemail = request.session['facultyemail']
    #facultypwd = request.session['facultypwd']
    if 'facultyemail' in request.session:
        #mail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            #pwd = request.session['facultypwd']
            try:
        #result = FacultyUser.objects.get(email=uemail, password=password)
                result2 = Complaint.objects.filter(status_id=3).values()
                print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2} )
            except User.DoesNotExist as e:
                print("sde")
                return render(request, 'dashboard')

    return redirect('home')


def ComplaintDetail(request):
    return render(request, 'ComplaintDetail.html')
