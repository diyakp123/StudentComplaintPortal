from django.shortcuts import render ,redirect
from django.http import HttpResponse
from Users.models import ContactUs, FacultyUser, User
from django.contrib import messages
from django.db import IntegrityError

from complaint.models import Complaint
# Create your views here.

def home(request): #when user is not authenticated
    if 'useremail' in request.session:
        mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            pwd = request.session['userpwd']
            try:
                result = User.objects.get(email=mail, password=pwd)
                return redirect('dashboard')
            except User.DoesNotExist as e:
                return render(request,'home')
            
    if 'facultyemail' in request.session:
        facultyemail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            password = request.session['facultypwd']
            try:
                result = FacultyUser.objects.get(facultyemail=facultyemail, password=password)
                return redirect('facultydashboard')

            except User.DoesNotExist as e:
                return redirect(request,'home')
            
    return render(request,'home.html')

def dashboard(request):   #once the user is authenticated, its homepage will be the dashboard
    if 'useremail' in request.session:
        mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            pwd = request.session['userpwd']
            try:
                result = User.objects.get(email=mail, password=pwd)
                return render(request,"dashboard.html")
            except User.DoesNotExist as e:
                return redirect(request,'home')
    
    if 'facultyemail' in request.session:
        facultyemail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            password = request.session['facultypwd']
            try:
                result = FacultyUser.objects.get(facultyemail=facultyemail, password=password)
                return redirect('facultydashboard')

            except User.DoesNotExist as e:
                return redirect(request,'home')

    return redirect('home')  

def studentlogin(request):
    #userid = request.
  #  if(userauthenticated)
 #       return dashboard
    if 'useremail' in request.session:
        mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            pwd = request.session['userpwd']
            try:
                result = User.objects.get(email=mail, password=pwd)
                return redirect('dashboard')
            except User.DoesNotExist as e:
                return redirect(request,'home')
            
    if 'facultyemail' in request.session:
        facultyemail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            password = request.session['facultypwd']
            try:
                result = FacultyUser.objects.get(facultyemail=facultyemail, password=password)
                return redirect('facultydashboard')

            except User.DoesNotExist as e:
                return redirect(request,'home')
            
    if(request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            result = User.objects.get(email=email, password=password)
            print("user exists")
            request.session['useremail'] = email
            request.session['userpwd'] = password
            return redirect('dashboard')
        except User.DoesNotExist as e:
            messages.info(request, 'Email or Password is wrong')
            #print("user doesnt exist")
            return redirect('studentlogin')
            '''if(request.method=='POST'):


         uemail = request.POST.get('email')
        password = request.POST.get('password')
        if(uemail=='abcd@gmail.com'):
            return render(request,'dashboard.html')
        else:
            return render(request,'login.html')''' #send a pop up or error message along with it
            

    return render(request,'studentlogin.html')

def registration(request):
      #  if(userauthenticated)
 #       return dashboard
    print("hi44")
    if(request.method=='POST'):  
        firstname = request.POST.get('fname')  #firstname = request.POST['fname'] can also write it like this
        lastname = request.POST.get('lname')
        Department = request.POST.get('Department')
        uemail = request.POST.get('email')
        password = request.POST.get('pswd')
        confirmpassword = request.POST.get('cpwd')

        print("hi")
        if(password==confirmpassword):
            print(uemail)
            try:
                user = User(first_name=firstname, last_name=lastname, email=uemail, department_id = Department, password=password )
                user.save()
                return redirect('studentlogin')
            except IntegrityError as e :
                messages.info(request, "Email taken")
                print("integrity error")
                return redirect('registration')
            
            '''  if User.objects.filter(email=uemail).exists:
                messages.info(request,"Email taken")
                
                return redirect('registration')
            else: 
                user = User(first_name=firstname, last_name=lastname, email=uemail, department_id = Department, password=password )
                user.save()
                print("hi1")
                return render('login') '''
            
        else:
            messages.info(request,"password and confirm password do not match")
            print("hi12213")
            return redirect('registration')
        
    if 'useremail' in request.session:
        mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            pwd = request.session['userpwd']
            try:
                result = User.objects.get(email=mail, password=pwd)
                return redirect('dashboard')

            except User.DoesNotExist as e:
                return render(request,'registration')
            
    if 'facultyemail' in request.session:
        facultyemail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            password = request.session['facultypwd']
            try:
                result = FacultyUser.objects.get(facultyemail=facultyemail, password=password)
                return redirect('facultydashboard')

            except User.DoesNotExist as e:
                return redirect(request,'home')
            

    return render(request,'registration.html')

def contactus(request):
    if(request.method == "POST"):
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']

        contactus = ContactUs(first_name = fname, last_name =lname, email=email,number=number,message=message)
        contactus.save()
        return render(request,'showdata.html', {'result' : "Message successfully sent"})

    return render(request,'contactUs.html')

def roles(request):
    if 'useremail' in request.session:
        mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            pwd = request.session['userpwd']
            try:
                result = User.objects.get(email=mail, password=pwd)
                return redirect('dashboard')
            except User.DoesNotExist as e:
                return redirect(request,'home')
            
    if 'facultyemail' in request.session:
        facultyemail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            password = request.session['facultypwd']
            try:
                result = FacultyUser.objects.get(facultyemail=facultyemail, password=password)
                return redirect('facultydashboard')

            except User.DoesNotExist as e:
                return redirect(request,'home')
    return render(request, 'roles.html')

def facultylogin(request):
    if 'useremail' in request.session:
        mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            pwd = request.session['userpwd']
            try:
                result = User.objects.get(email=mail, password=pwd)
                return redirect('dashboard')
            except User.DoesNotExist as e:
                return redirect(request,'home')
            
    if 'facultyemail' in request.session:
        facultyemail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            password = request.session['facultypwd']
            try:
                result = FacultyUser.objects.get(facultyemail=facultyemail, password=password)
                return redirect('facultydashboard')

            except User.DoesNotExist as e:
                return redirect(request,'home')
            
    if(request.method == 'POST'):
        facultyemail = request.POST.get('facultyemail')
        password = request.POST.get('facultypwd')
        try:
            print(password)
            print(FacultyUser.objects.filter(password=password).values())
            result = FacultyUser.objects.get( password=password,facultyemail=facultyemail)
            print("faculty credentials right")
            request.session['facultyemail'] = facultyemail
            request.session['facultypwd'] = password
            return redirect('facultydashboard')
        except FacultyUser.DoesNotExist as e:
            messages.info(request, 'Email or Password is wrong')
            #print("user doesnt exist")
            return redirect('facultylogin')
        
   
            

    return render(request,'facultylogin.html')

def Facultydashboard(request):
   # facultyemail = request.session['facultyemail']
    #facultypwd = request.session['facultypwd']
    if 'facultyemail' in request.session:
        #mail = request.session['facultyemail']  # mail = request.session.get('useremail', request.GET)
        if 'facultypwd' in request.session:
            #pwd = request.session['facultypwd']
            try:
        #result = FacultyUser.objects.get(email=uemail, password=password)
                result2 = Complaint.objects.values()
                print(result2)
                return render(request, 'facultydashboard.html', {'result' : result2} )
            except User.DoesNotExist as e:
                print("sde")
                return render(request, 'dashboard')

    return redirect('home')
    


def studentlogout(request):
    try:
        del request.session['useremail']
        del request.session['userpwd']
        return render(request,'studentlogout.html')  
    except KeyError as e:
        return redirect('home')
      
def facultylogout(request):
    try:
        del request.session['facultyemail']
        del request.session['facultypwd']
        return render(request,'facultylogout.html')  
    except KeyError as e:
        return redirect('home')