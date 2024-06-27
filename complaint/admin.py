from django.contrib import admin

from .models import Category, Complaint, ComplaintStatus,Feedback
# Register your models here.
admin.site.register(Category)
admin.site.register(Complaint)
admin.site.register(ComplaintStatus)
admin.site.register(Feedback)