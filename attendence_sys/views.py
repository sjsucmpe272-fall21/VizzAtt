from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import Student, Attendence
from .filters import AttendenceFilter

from .recognizer import Recognizer
from datetime import date

@login_required(login_url = 'login')
def home(request):
    studentForm = CreateStudentForm()

    if request.method == 'POST':
        studentForm = CreateStudentForm(data = request.POST, files=request.FILES)
        stat = False 
        try:
            student = Student.objects.get(registration_id = request.POST['registration_id'])
            stat = True
        except:
            stat = False
        if studentForm.is_valid() and (stat == False):
            studentForm.save()
            name = studentForm.cleaned_data.get('firstname') +" " +studentForm.cleaned_data.get('lastname')
            messages.success(request, 'Student ' + name + ' was successfully added.')
            return redirect('home')
        else:
            messages.error(request, 'Student with Registration Id '+request.POST['registration_id']+' already exists.')
            return redirect('home')

    context = {'studentForm':studentForm}
    return render(request, 'home.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')

    context = {}
    return render(request, 'login.html', context)

@login_required(login_url = 'login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
def updateStudentRedirect(request):
    context = {}
    if request.method == 'POST':
        try:
            reg_id = request.POST['reg_id']
            branch = request.POST['branch']
            student = Student.objects.get(registration_id = reg_id, branch = branch)
            updateStudentForm = CreateStudentForm(instance=student)
            context = {'form':updateStudentForm, 'prev_reg_id':reg_id, 'student':student}
        except:
            messages.error(request, 'Student Not Found')
            return redirect('home')
    return render(request, 'student_update.html', context)

@login_required(login_url = 'login')
def updateStudent(request):
    if request.method == 'POST':
        context = {}
        try:
            print(request.POST)
            student = Student.objects.get(registration_id = request.POST['registration_id'])
            print(student.firstname)
            updateStudentForm = CreateStudentForm(data = request.POST, files=request.FILES, instance = student)
            if updateStudentForm.is_valid():
                updateStudentForm.save()
                messages.success(request, 'Updated successfully')
                return redirect('home')
        except:
            messages.error(request, 'Updation Unsucessfull')
            return redirect('home')
    return render(request, 'student_update.html', context)


@login_required(login_url = 'login')
def takeAttendence(request):
    if request.method == 'POST':
        details = {
            'branch':request.POST['branch'],
            'section':request.POST['section'],
            'period':request.POST['period'],
            'faculty':request.user.faculty
            }
        if Attendence.objects.filter(date = str(date.today()),branch = details['branch'], section = details['section'],period = details['period']).count() != 0 :
            messages.error(request, "Attendence already recorded.")
            return redirect('home')
        else:
            students = Student.objects.filter(branch = details['branch'], section = details['section'])
            names = Recognizer(details)
            for student in students:
                if str(student.registration_id) in names:
                    attendence = Attendence(Faculty_Name = request.user.faculty, 
                        Student_ID = str(student.registration_id), 
                        period = details['period'], 
                        branch = details['branch'], 
                        section = details['section'],
                        status = 'Present'
                    )
                    attendence.save()
                else:
                    attendence = Attendence(Faculty_Name = request.user.faculty, 
                        Student_ID = str(student.registration_id), 
                        period = details['period'],
                        branch = details['branch'], 
                        section = details['section']
                    )
                    attendence.save()
            attendences = Attendence.objects.filter(date = str(date.today()),branch = details['branch'], section = details['section'],period = details['period'])
            context = {"attendences":attendences, "ta":True}
            messages.success(request, "Attendance recorded successfully")
            return render(request, 'attendance.html', context)        
    context = {}
    return render(request, 'home.html', context)

def searchAttendence(request):
    attendences = Attendence.objects.all()
    myFilter = AttendenceFilter(request.GET, queryset=attendences)
    attendences = myFilter.qs
    context = {'myFilter':myFilter, 'attendences': attendences, 'ta':False}
    return render(request, 'attendance.html', context)


def facultyProfile(request):
    faculty = request.user.faculty
    form = FacultyForm(instance = faculty)
    context = {'form':form}
    return render(request, 'facultyForm.html', context)


def updateFaculty(request):
    if request.method == 'POST':
        context = {}
        try:
            print(request.POST)
            faculty = Faculty.objects.get(email = request.POST['email'])
            print(faculty.firstname)
            updateFacultyForm = FacultyForm(data = request.POST, files=request.FILES, instance = faculty)
            if updateFacultyForm.is_valid():
                updateFacultyForm.save()
                messages.success(request, 'Updated successfully')
                return redirect('home')
        except:
            messages.error(request, 'Updation Unsucessfull')
            return redirect('home')
    return render(request, 'facultyForm.html', context)