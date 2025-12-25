from django.contrib import admin
from django.urls import path, include
from core.views import login_view, logout_view
from teacher.views import teacher_dashboard, mark_attendance
from student.views import student_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('teacher/dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('teacher/mark-attendance/', mark_attendance, name='mark_attendance'),
    path('logout/', logout_view, name='logout'),
]
