from django.contrib import admin
from django.urls import path, include
from core.views import login_view, logout_view
from teacher.views import teacher_dashboard
from student.views import student_dashboard

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Login (Core App)
    path('', login_view, name='login'),

    # Teacher Dashboard
    path('teacher/dashboard/', teacher_dashboard, name='teacher_dashboard'),

    # Student Dashboard
    path('student/dashboard/', student_dashboard, name='student_dashboard'),

     path('logout/', logout_view, name='logout'),
]
