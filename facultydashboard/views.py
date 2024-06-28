from django.shortcuts import redirect, render
import datetime
from datetime import datetime
from Users.models import User
from Users.views import Facultydashboard
from complaint.models import Category, Complaint, ComplaintStatus

# Create your views here.


def user(request):
    return render(request, 'facultydashboard.html')


def FacultyAllComplaints(request):
   # facultyemail = request.session['facultyemail']
    #facultypwd = request.session['facultypwd']
    if 'facultyemail' in request.session:
        #mail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            #pwd = request.session['facultypwd']
            try:
        #result = FacultyUser.objects.get(email=uemail, password=password)
                result2 = Complaint.objects.values()
                #print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2, 'val' : 'All Complaints'} )
            except User.DoesNotExist as e:
                print("sde")
                return render(request, 'dashboard')

    return redirect('home')


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
                #print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2, 'val' : 'All Solved Complaints'} )
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
                #print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2, 'val' : 'All Unsolved Complaints'} )
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
                #print(result2)
                return render(request, 'FacultyComplaint.html', {'result' : result2, 'val' : 'All InProgress Complaints'} )
            except User.DoesNotExist as e:
                print("sde")
                return render(request, 'dashboard')

    return redirect('home')


def FacultyFilterData(request):
    if 'facultyemail' in request.session:
        if 'facultypwd' in request.session:
           try:
                #email = request.POST.get('email')
                #password = request.POST.get('password') 
                #result = User.objects.get(email=email, password=password)

                status = request.POST.get('status')
                category = request.POST.get('ComplaintType') 

                if status=="All InProgress Complaints":
                    status_id=3
                    statusobj = ComplaintStatus.objects.get(id=status_id)
                    result2 = Complaint.objects.filter(status=statusobj, category=category).values()
                elif status=="All Solved Complaints":
                    status_id=1
                    statusobj = ComplaintStatus.objects.get(id=status_id)
                    result2 = Complaint.objects.filter(status=statusobj, category=category).values()
                elif status=="All Unsolved Complaints":
                    status_id=2
                    statusobj = ComplaintStatus.objects.get(id=status_id)
                    result2 = Complaint.objects.filter(status=statusobj, category=category).values()
                else:
                    result2 = Complaint.objects.filter(category=category).values()
                print(status)
                return render(request, 'FacultyComplaint.html', {'result' : result2, 'val' : status} )
           except User.DoesNotExist as e:
                print("sde")
                return render(request, 'dashboard')

    return redirect('home')


def ComplaintDetail(request, id):

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
    
    ''' datetimedata = result2[0]['complaint_dateTime']
    dd = datetime(datetimedata)
   
    print( dd.date)
    '''
    cid = result2[0]['id']
   
    
    
    if result2[0]['anonymous'] == True:
        print("hey")
        userdet = "anonymous"
        depts = "anonymous"

    return render(request, 'ComplaintDetail.html',{ 'desc': description ,'type' : type , 'user' : userdet, 'deptobj' : depts,'status' : status, 'cid':cid})




def ComplaintReceived(request,id):
    complaint = complaint = Complaint.objects.get(id = id)
    complaint.status = ComplaintStatus.objects.get(status_name="inprogress")
    complaint.save()
    return redirect('/')
