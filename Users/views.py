from django.shortcuts import render ,redirect
from django.http import HttpResponse
from Users.models import User
from django.contrib import messages
from django.db import IntegrityError
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
                return render(request,'home')
    return redirect('home')

def login(request):
    #userid = request.
  #  if(userauthenticated)
 #       return dashboard
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
            return redirect('login')
            '''if(request.method=='POST'):


         uemail = request.POST.get('email')
        password = request.POST.get('password')
        if(uemail=='abcd@gmail.com'):
            return render(request,'dashboard.html')
        else:
            return render(request,'login.html')''' #send a pop up or error message along with it
    if 'useremail' in request.session:
        mail = request.session['useremail']  # mail = request.session.get('useremail', request.GET)
        if 'userpwd' in request.session:
            pwd = request.session['userpwd']
            try:
                result = User.objects.get(email=mail, password=pwd)
                return redirect('dashboard')

            except User.DoesNotExist as e:
                return render(request,'login')
            

    return render(request,'login.html')

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
                return render(request,'login.html')
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
    return render(request,'registration.html')

def contactus(request):
    return render(request,'contactUs.html')
