from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Teacher,Subjects,Attendance
from student.models import Student,Branch
from django.contrib import messages

@login_required
def teacher_dashboard(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        return redirect('login')
    
    return render(request, 'teacher/teacher_dashboard.html', {
        'teacher': teacher})




@login_required
def mark_attendance(request):
    subjects = Subjects.objects.all()
    branches = Branch.objects.all()
    students = []

    
    selected_subject = None
    selected_branch = None
    date = time = duration = None

    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        branch_id = request.POST.get('branch')
        date = request.POST.get('date')
        time = request.POST.get('time')
        duration = request.POST.get('duration')

        if branch_id:
            selected_branch = Branch.objects.get(id=branch_id)
            students = Student.objects.filter(branch=selected_branch)

        if subject_id:
            selected_subject = Subjects.objects.get(id=subject_id)

        
        if 'submit_attendance' in request.POST:
            already_marked = Attendance.objects.filter(
                subject=selected_subject,
                date=date,
                time=time
            ).exists()

            if already_marked:
                messages.error(
                    request,
                    "Attendance already marked for this subject and time ❌"
                )
            else:
                for student in students:
                    status = request.POST.get(
                        f"present_{student.id}"
                    ) == "on"

                    Attendance.objects.create(
                        student=student,
                        subject=selected_subject,
                        date=date,
                        time=time,
                        duration=duration,
                        status=status
                    )

                messages.success(
                    request,
                    "Attendance saved successfully ✅"
                )

            return redirect('teacher_dashboard')

    return render(request, 'teacher/mark_attendance.html', {
        'subjects': subjects,
        'branches': branches,
        'students': students,
        'selected_subject': selected_subject,
        'selected_branch': selected_branch,
        'date': date,
        'time': time,
        'duration': duration
    })
