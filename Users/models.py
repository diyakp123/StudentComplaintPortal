from django.db import models

# Create your models here.
class registration(models.Model):
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email = models.EmailField(max_length=35)
    department_id = models.IntegerField()
    password = models.CharField(max_length=40)
    confirm_password = models.CharField(max_length=40)


class login(models.Model):
    email = models.EmailField(max_length=35)
    password = models.CharField(max_length=40)





