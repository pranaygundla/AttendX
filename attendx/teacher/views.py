from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Teacher

@login_required
def teacher_dashboard(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        return redirect('login')
    
    return render(request, 'teacher/teacher_dashboard.html', {
        'teacher': teacher})

