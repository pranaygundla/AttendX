from django.db import models
from django.contrib.auth.models import User
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
    subjects = models.ManyToManyField(
        'Subjects',
        related_name='teachers',
        verbose_name='Subjects taught'
        , blank=True,
    )

    def __str__(self):
        return self.teacher_name