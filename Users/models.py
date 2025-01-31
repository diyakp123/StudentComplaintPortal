from django.db import models

# Create your models here.


class Department(models.Model):
    dept_id = ('deptid', models.BigAutoField(auto_created=True, primary_key=True, serialize=False))
    dept_name = models.CharField(max_length=30)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    password = models.CharField(max_length=40)
#    confirm_password = models.CharField(max_length=40)


class FacultyUser(models.Model):
    facultyid = ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False))
    facultyemail = models.EmailField(max_length=50, unique=True, default="faculty@complaintportal.com")
    password = models.CharField(max_length=40, default="1234")


class ContactUs(models.Model):
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    number = models.IntegerField()
    message = models.TextField()

#class login(models.Model):
#    email = models.EmailField(max_length=35)
#    password = models.CharField(max_length=40)








