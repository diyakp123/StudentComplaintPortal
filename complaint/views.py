from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render

from Users.models import Department, User
from Users.views import dashboard
from complaint.models import Category, Complaint, Feedback

# Create your views here.


def user(request):
    return dashboard(request)

def feedback(request):

    if(request.method == "POST"):
        uemail = request.session['useremail']
        password = request.session['userpwd']

        fname = request.POST['fname']
        email = request.POST['email']
        message = request.POST['message']
        complaintid = request.session['complaintid']
        try:
            result = User.objects.get(email=uemail, password=password)
            complaint = Complaint.objects.get(id = complaintid)
            feedback = Feedback(fullname= fname, email=email, complaintid=complaintid,opinion=message)
            feedback.save()
            return render(request, 'showdata.html',{'result' : "Feedback successfully sent"})

        except User.DoesNotExist as e:
            print("e")
            return render(request, 'Feedback.html')
      

    return render(request, 'Feedback.html')

def complaint(request):
    return render(request,'complaint.html')


def StudentComplaintHistory(request):
    if 'useremail' in request.session:
        #mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            #pwd = request.session['userpwd']
            uemail = request.session['useremail']
            password = request.session['userpwd']
            try:
                result = User.objects.get(email=uemail, password=password)
                result2 = Complaint.objects.filter(student=result).values()
                print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2} )
            except User.DoesNotExist as e:
                print("sde")
                return redirect( 'dashboard')
    
    return redirect( 'dashboard')



def thankyou(request):
    if(request.method=='POST'): 
        if request.POST['complaint'] != "":
            complaintType = request.POST['ComplaintType']
            complaintText = request.POST['complaint']
            anon = False
            if "anonymous" in request.POST:
                if(request.POST.get('anonymous') == "on"):
                    anon = True

            print(anon)
            print("hello")
            uemail = request.session['useremail']
            password = request.session['userpwd']
            try:
                result = User.objects.get(email=uemail, password=password)
                print("hello22321")
                print(result)
                

                result2 = Category.objects.get(id = complaintType)
                
                print(result2)
                category = result2
                
                complaint = Complaint(student=result,category=category , description=complaintText, anonymous=anon)
                complaint.save()
                return render(request,"thankyou.html")
                 
            except User.DoesNotExist as e:
                return redirect('complaint')
            
    messages.info(request, "Empty Complaint Field")
    print("Empty Complaint Field")
    return redirect('complaint')


def StudentInprogressComplaints(request):
    if 'useremail' in request.session:
        #mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            #pwd = request.session['userpwd']
            uemail = request.session['useremail']
            password = request.session['userpwd']
            try:
                result = User.objects.get(email=uemail, password=password)
                result2 = Complaint.objects.filter(student=result,status=3).values()
                print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2} )
            except User.DoesNotExist as e:
                print("sde")
                return redirect( 'dashboard')
    
    return redirect( 'dashboard')

def StudentUnsolvedComplaints(request):
    if 'useremail' in request.session:
        #mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            #pwd = request.session['userpwd']
            uemail = request.session['useremail']
            password = request.session['userpwd']
            try:
                result = User.objects.get(email=uemail, password=password)
                result2 = Complaint.objects.filter(student=result,status=2).values()
                print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2} )
            except User.DoesNotExist as e:
                print("sde")
                return redirect( 'dashboard')
    
    return redirect( 'dashboard')

def StudentSolvedComplaints(request):
    if 'useremail' in request.session:
        #mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            #pwd = request.session['userpwd']
            uemail = request.session['useremail']
            password = request.session['userpwd']
            try:
                result = User.objects.get(email=uemail, password=password)
                result2 = Complaint.objects.filter(student=result,status=1).values()
                print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2} )
            except User.DoesNotExist as e:
                print("sde")
                return redirect( 'dashboard')
    
    return redirect( 'dashboard')

def ComplaintDetail(request):
    return render(request, 'ComplaintDetail.html')
