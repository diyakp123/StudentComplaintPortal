from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render

from Users.models import Department, User
from Users.views import dashboard
from complaint.models import Category, Complaint

# Create your views here.


def user(request):
    return dashboard(request)

def feedback(request):
    return render(request, 'Feedback.html')

def complaint(request):
    return render(request,'complaint.html')

def FacultyComplaint(request):
    uemail = request.session['useremail']
    password = request.session['userpwd']
    try:
        result = User.objects.get(email=uemail, password=password)
        result2 = Complaint.objects.filter(student=result).values()
        print(result2)
        return render(request, 'FacultyComplaint.html', {'result' : result2} )
    except User.DoesNotExist as e:
        print("sde")
    
    return render(request, 'dashboard')

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





def history(request):
    my_user = request.user
      #to get aa complaints stored in database table 'complaint' 

    return render(request, 'history.html')