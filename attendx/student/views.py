from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from teacher.models import Attendance
from .models import Student

@login_required
def student_dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        return redirect('login')

    records = Attendance.objects.filter(student=student)

    # Overall calculation
    total_duration = sum(r.duration for r in records)
    present_duration = sum(r.duration for r in records if r.status)

    absent_duration = total_duration - present_duration

    present_percentage = round(
        (present_duration / total_duration) * 100, 2
    ) if total_duration > 0 else 0

    absent_percentage = round(100 - present_percentage, 2) if total_duration > 0 else 0

    # ✅ Subject-wise calculation
    subject_data = {}

    for r in records:
        subject = r.subject.subject_name

        if subject not in subject_data:
            subject_data[subject] = {
                'total': 0,
                'present': 0
            }

        subject_data[subject]['total'] += r.duration
        if r.status:
            subject_data[subject]['present'] += r.duration

    subject_attendance = []
    for subject, data in subject_data.items():
        total = data['total']
        present = data['present']
        percent = round((present / total) * 100, 2) if total > 0 else 0

        subject_attendance.append({
            'subject': subject,
            'present_percentage': percent,
            'absent_percentage': round(100 - percent, 2),
            'total_duration': total
        })

    return render(request, 'student/student_dashboard.html', {
        'student': student,
        'present_percentage': present_percentage,
        'absent_percentage': absent_percentage,
        'present_duration': present_duration,
        'absent_duration': absent_duration,
        'total_duration': total_duration,
        'subject_attendance': subject_attendance
    })
