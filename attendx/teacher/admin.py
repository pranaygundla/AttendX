from django.contrib import admin
from .models import Teacher, Subjects,Attendance


# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subjects)
admin.site.register(Attendance)