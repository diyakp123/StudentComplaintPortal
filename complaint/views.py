from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render

from Users.models import Department, User
from Users.views import dashboard
from complaint.models import Category, Complaint, ComplaintStatus, Feedback

# Create your views here.


def user(request):
    return dashboard(request)

def feedback(request,id):
    return render(request, 'Feedback.html', {'id' : id})

def feedbacksubmit(request):
     if(request.method == "POST"):
        uemail = request.session['useremail']
        password = request.session['userpwd']

        fname = request.POST['fullname']
        email = request.POST['eid']
        message = request.POST['opinion']
        complaintid = request.POST['id']
        print(complaintid)
        try:
            result = User.objects.get(email=uemail, password=password)
            complaint = Complaint.objects.get(id = complaintid)
            feedback = Feedback(fullname= fname, email=result, complaintid=complaint,opinion=message)
            feedback.save()
            return render(request, 'showdata.html',{'result' : "Feedback successfully sent"})

        except User.DoesNotExist as e:
            print("e")
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
                return render(request, 'StudentComplaint.html', {'result' : result2, 'val' : 'All Complaints'} )
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
                result2 = Complaint.objects.filter(student=result,status_id=3).values()
                print(result2)
                return render(request, 'StudentComplaint.html', {'result' : result2, 'val' : 'All InProgress Complaints'} )
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
                result2 = Complaint.objects.filter(student=result,status_id=2).values()
                print(result2)
                return render(request, 'StudentComplaint.html', {'result' : result2, 'val' : 'All Unsolved Complaints'} )
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
                result2 = Complaint.objects.filter(student=result,status_id=1).values()
                print(result2)
                return render(request, 'StudentComplaint.html', {'result' : result2 , 'val' : 'All Solved Complaints'} )
            except User.DoesNotExist as e:
                print("sde")
                return redirect( 'dashboard')
    
    return redirect( 'dashboard')


def FilterData(request):
    if 'useremail' in request.session:
        #mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            #pwd = request.session['userpwd']
            uemail = request.session['useremail']
            password = request.session['userpwd']
            try:
                result = User.objects.get(email=uemail, password=password)
              

                status = request.POST.get('status')
                category = request.POST.get('ComplaintType') 
              
                print(status)

                if status=="All InProgress Complaints":
                    status_id=3
                    statusobj = ComplaintStatus.objects.get(id=status_id)
                    result2 = Complaint.objects.filter(student=result,status=statusobj, category=category).values()
                elif status=="All Solved Complaints":
                    status_id=1
                    statusobj = ComplaintStatus.objects.get(id=status_id)
                    result2 = Complaint.objects.filter(student=result,status=statusobj, category=category).values()
                elif status=="All Unsolved Complaints":
                    status_id=2
                    statusobj = ComplaintStatus.objects.get(id=status_id)
                    result2 = Complaint.objects.filter(student=result,status=statusobj, category=category).values()
                else:
                    result2 = Complaint.objects.filter(student=result,category=category).values()
                
                print(category)
                print(result2)
                return render(request, 'StudentComplaint.html', {'result' : result2, 'val' : status} )
            except User.DoesNotExist as e:
                print("sde")
                return render(request, 'dashboard')

    return redirect('home')




def StudentComplaintDetail(request, id):

    result2 = Complaint.objects.filter(id=id).values()  
    print(result2)

    description = result2[0]['description']

    userdetails = User.objects.get(id=result2[0]['student_id'])
    userdet =  userdetails.first_name

    departmentobj = userdetails.department
    depts =  departmentobj.dept_name

    cattype = Category.objects.get(id=result2[0]['category_id'])
    type = cattype.category_name

    statustype = ComplaintStatus.objects.get(id=result2[0]['status_id'])
    status = statustype.status_name
    
    cid = result2[0]['id']
    print(cid)
    ''' datetimedata = result2[0]['complaint_dateTime']
    dd = datetime(datetimedata)
   
    print( dd.date)
    '''
    
    
    
    if result2[0]['anonymous'] == True:
        print("hey")
        userdet = "anonymous"
        depts = "anonymous"

    return render(request, 'StudentComplaintDetail.html',{ 'desc': description ,'type' : type , 'user' : userdet, 'deptobj' : depts,'status' : status, 'cid' : cid})


def studentlogout(request):
    try:
        del request.session['useremail']
        del request.session['userpwd']
        return render(request,'studentlogout.html')  
    except KeyError as e:
        return redirect('home')