from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from teacher.models import Teacher
from student.models import Student
from django.contrib.auth import logout
from django.shortcuts import redirect




def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        role=request.POST['role']

        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)

            if role=='teacher' and Teacher.objects.filter(user=user).exists():
                return redirect('teacher_dashboard')
            
            elif role=='student' and Student.objects.filter(user=user).exists():
                return redirect('student_dashboard')
            
            else:
                return render(request,'core/login.html',
                              {
                                  'error':'Role mismatch'
                              })
        
        return render(request,'core/login.html',
                              {
                                  'error':'Invalid user name and password'
                              })
        

    return render(request,'core/login.html' )

def logout_view(request):
    logout(request)
    return redirect('login')