from django.db import models
from django.contrib.auth.models import User
from student.models import Student


# Create your models here.
class Subjects(models.Model):
    subject_name=models.CharField(max_length=100)
    subject_code=models.CharField(max_length=20)

    def __str__(self):
        return self.subject_name



class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    teacher_name=models.CharField(max_length=100)
    teacher_email = models.EmailField(max_length=100, blank=True, null=True)
    subjects = models.ManyToManyField(Subjects, blank=True)

    def __str__(self):
        return self.teacher_name


class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    status=models.BooleanField()
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.student.student_name} - {self.subject.subject_name}"