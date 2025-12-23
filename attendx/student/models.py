from django.db import models
from django.contrib.auth.models  import User


class Branch(models.Model):
    branch_name=models.CharField(max_length=100)
    branch_code=models.CharField(max_length=20)

    def __str__(self):
        return self.branch_name


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100, blank=True, null=True)
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.student_name

