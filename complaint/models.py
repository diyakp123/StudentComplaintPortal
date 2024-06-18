from django.db import models

from Users.models import User

# Create your models here.


class Faculty(models.Model):
    faculty_id = ('facultyid', models.BigAutoField(auto_created=True, primary_key=True, serialize=False))
    faculty_name = models.CharField(max_length=30)

class Category(models.Model):
    category_id = ('categoryid', models.BigAutoField(auto_created=True, primary_key=True, serialize=False))
    category_name = models.CharField(max_length=30)

class ComplaintStatus(models.Model):
    status_id = ('status_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False))
    status_name = models.CharField(max_length=30)

class Complaint(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint_dateTime = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    anonymous = models.BooleanField()
    status = models.ForeignKey(ComplaintStatus, on_delete=models.CASCADE)

