from django.contrib import admin

from .models import ContactUs, User, Department, FacultyUser

# Register your models here.

admin.site.register(User)
admin.site.register(Department)
admin.site.register(FacultyUser)
admin.site.register(ContactUs)
