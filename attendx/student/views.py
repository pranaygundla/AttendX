from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from student.models import Student

@login_required
def student_dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        return redirect('login')

    return render(request, 'student/student_dashboard.html', {
        'student': student
    })