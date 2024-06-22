from django.shortcuts import render, redirect
from .models import Gender, Year, Course, Student, User, Academic, Section
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator


def indexgender(request):
    genders = Gender.objects.all()

    context = {
        'genders': genders
    }

    return render(request, 'gender/index.html', context)

def creategender(request):
    return render(request, 'gender/create.html')

def storegender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender)
    messages.success(request,'Successfully Save!')
    return redirect('/genders')

def showgender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    context = {
        'gender' : gender,
    }

    return render(request, 'gender/show.html', context)

def editgender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    context = {
        'gender' : gender,
    }

    return render(request, 'gender/edit.html', context)

def updategender(request, gender_id):
    
    gender = request.POST.get('gender')
    Gender.objects.filter(pk=gender_id).update(gender=gender)
    messages.success(request, 'Gender Successfully Updated')
    return redirect('/genders')


def deletegender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    context = {
        'gender' : gender,
    }

    return render(request, 'gender/delete.html', context)

def destroygender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete()
    messages.success(request,'Successfully Deleted.')
    return redirect('/genders')


def index_user(request):
    users = User.objects.select_related('gender')

    context={
        'users': users,
    }
    return render(request, 'user/index.html', context)

def create_user(request):
    genders = Gender.objects.all()

    context = {
        'genders':genders
    }
    return render(request, 'user/create.html', context)

def store_user(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    genderId = request.POST.get('gender_id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirm_password')

   
    if password == confirmPassword:
        encryptedPassword = make_password(password)

        User.objects.create(
            first_name=firstName,
            middle_name=middleName,
            last_name=lastName,
            age=age,
            birth_date=birthDate,
            gender_id=genderId,
            username=username,
            password= encryptedPassword
            )
        messages.success(request, 'success')

        return redirect('/user')
    else:
        messages.error(request, 'error')
        return redirect('/create')

def show_user(request, user_id):
    user = User.objects.get(pk=user_id)

    context = {
        'user': user,
        'first_name':user,
    }
    return render(request, 'user/show.html', context)

def edit_user(request, user_id):
    genders = Gender.objects.all()
    user = User.objects.get(pk=user_id)
    context = {
        'user': user,
        'genders':genders,
    }

    return render(request, 'user/edit.html', context)

def update_user(request, user_id):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    genderid = request.POST.get('gender_id')
    username = request.POST.get('username')

    User.objects.filter(pk=user_id).update(first_name = firstName, middle_name = middleName, last_name = lastName, age = age, birth_date = birthDate, gender_id = genderid, username = username)

    messages.success(request, 'User successfully updated.')

    return redirect ('/users')

def delete_user(request, user_id):
    user = User.objects.get(pk=user_id) 

    context = {
        'user': user,
    }

    return render(request, 'user/delete.html', context)

def destroy_user(request, user_id):
    User.objects.filter(pk=user_id).delete()
    messages.success(request, 'User successfully deleted.')

    return redirect('/users')
def index_section(request):
    sections = Section.objects.all() # SELECT * FROM genders
    
    context = {
        'sections': sections
    }

    return render(request, 'section/index.html', context)

def create_section(request):
    return render(request, 'section/create.html')

def store_section(request):
    section = request.POST.get('section')
    Section.objects.create(section=section) # INSERT INTO genders(gender) VALUES(gender)
    messages.success(request, 'Section succesfully saved.')
    return redirect('/sections')
    
def show_section(request, section_id):
    section = Section.objects.get(pk=section_id) # SELECT * FROM genders WHERE id = gender_id

    context = {
        'section': section,
    }

    return render(request, 'section/show.html', context)

def edit_section(request, section_id):
    section = Section.objects.get(pk=section_id) # SELECT * FROM genders WHERE id = gender_id

    context = {
        'section': section,
    }

    return render(request, 'section/edit.html', context)

def update_section(request, section_id):
    section = request.POST.get('section')

    Section.objects.filter(pk=section_id).update(section=section)
    messages.success(request, 'Section successfully updated.')

    return redirect('/sections')

def delete_section(request, section_id):
    section = Section.objects.get(pk=section_id) # SELECT * FROM genders WHERE id = gender_id

    context = {
        'section': section,
    }

    return render(request, 'section/delete.html', context)

def destroy_section(request, section_id):
    Section.objects.filter(pk=section_id).delete()
    messages.success(request, 'Section successfully deleted.')

    return redirect('/sections')

def index_year(request):
    query = request.GET.get('year_list')
    if query:
        years = Year.objects.filter(year__icontains=query)
    else:
        years = Year.objects.all()

    paginator = Paginator(years, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'years': page_obj,
        'query': query

    }
    
    return render(request, 'year/index.html', context)

def create_year(request):
    return render(request, 'year/create.html')

def store_year(request):
    year = request.POST.get('year')
    Year.objects.create(year=year) # INSERT INTO genders(gender) VALUES(year)
    messages.success(request, 'Years succesfully saved.')
    return redirect('/years')
    
def show_year(request, year_id):
    year = Year.objects.get(pk=year_id) # SELECT * FROM genders WHERE id = year_id

    context = {
        'year': year,
    }

    return render(request, 'year/show.html', context)

def edit_year(request, year_id):
    year = Year.objects.get(pk=year_id) # SELECT * FROM genders WHERE id = year_id

    context = {
        'year': year,
    }

    return render(request, 'year/edit.html', context)

def update_year(request, year_id):
    year = request.POST.get('year')

    Year.objects.filter(pk=year_id).update(year=year)
    messages.success(request, 'Gender successfully updated.')

    return redirect('/years')

def delete_year(request, year_id):
    year = Year.objects.get(pk=year_id) # SELECT * FROM genders WHERE id = year_id

    context = {
        'year': year,
    }

    return render(request, 'year/delete.html', context)

def destroy_year(request, year_id):
    Year.objects.filter(pk=year_id).delete()
    messages.success(request, 'YearLevel successfully deleted.')

    return redirect('/years')

def index_course(request):
    courses = Course.objects.all() # SELECT * FROM years
    
    context = {
        'courses': courses
    }
    
    return render(request, 'course/index.html', context)

def create_course(request):
    return render(request, 'course/create.html')

def store_course(request):
    course = request.POST.get('course')
    Course.objects.create(course=course) # INSERT INTO genders(gender) VALUES(year)
    messages.success(request, 'Course succesfully saved.')
    return redirect('/courses')
    
def show_course(request, course_id):
    course = Course.objects.get(pk=course_id) # SELECT * FROM genders WHERE id = year_id

    context = {
        'course': course,
    }

    return render(request, 'course/show.html', context)

def edit_course(request, course_id):
    course = Course.objects.get(pk=course_id) # SELECT * FROM genders WHERE id = year_id

    context = {
        'course': course,
    }

    return render(request, 'course/edit.html', context)

def update_course(request, course_id):
    course = request.POST.get('course')

    Course.objects.filter(pk=course_id).update(course=course)
    messages.success(request, 'Course successfully updated.')

    return redirect('/courses')

def delete_course(request, course_id):
    course = Course.objects.get(pk=course_id) # SELECT * FROM genders WHERE id = year_id

    context = {
        'course': course,
    }

    return render(request, 'course/delete.html', context)

def destroy_course(request, course_id):
    Course.objects.filter(pk=course_id).delete()
    messages.success(request, 'Course successfully deleted.')

    return redirect('/courses')

def index_student(request):
    students = Student.objects.select_related('gender', 'course', 'year')
    query = request.GET.get('students')
    if query:
        students = Student.objects.filter(first_name__icontains=query)
    else:
        students = Student.objects.all()

    paginator = Paginator(students, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'students': page_obj,
        'query' : query,
    }

    return render(request, 'student/index.html', context)

def create_student(request):
    genders = Gender.objects.all()
    sections = Section.objects.all()

    context = {
    'genders': genders,
    'sections': sections
    }

    return render(request, 'student/create.html', context)

def store_student(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    genderid = request.POST.get('gender_id')
    sectionid = request.POST.get('section_id')
    address = request.POST.get('address')

    Student.objects.create(first_name = firstName, middle_name = middleName, last_name = lastName, age = age, gender_id = genderid, section_id = sectionid, address= address)

    messages.success(request, 'Profile succesfully saved.')

    return redirect('/academics/create')

def show_student(request, student_id):
    gender = Gender.objects.all()
    section= Section.objects.all()
    student = Student.objects.get(pk=student_id)

    context = {
        'student': student,
        'gender' : gender,
        'section': section,
    }

    return render(request, 'student/show.html', context)

def edit_student(request, student_id):
    gender = Gender.objects.all()
    section = Section.objects.all()
    student = Student.objects.get(pk=student_id)

    context = {
        'student': student,
        'gender' : gender,
        'section': section,
    }

    return render(request, 'student/show.html', context)

def update_student(request, student_id):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    genderid = request.POST.get('gender_id')
    sectionid = request.POST.get('section_id')
    schoolyear = request.POST.get('school_year')

    Student.objects.filter(pk=student_id).update(first_name = firstName, middle_name = middleName, last_name = lastName, age = age, gender_id = genderid, section_id = sectionid, school_year= schoolyear)

    messages.success(request, 'Profile succesfully Update.')

    return redirect('/students')

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id) 

    context = {
        'student': student,
    }

    return render(request, 'student/delete.html', context)

def destroy_student(request, student_id):
    Student.objects.filter(pk=student_id).delete()
    messages.success(request, 'Profile successfully deleted.')

    return redirect('/students')

def index_academic(request):
    academics = Academic.objects.select_related('course', 'year')
    query = request.GET.get('academic_list')
    if query:
        academics = Academic.objects.filter(course_id__icontains=query)
    else:
        academics = Academic.objects.all()

    paginator = Paginator(academics, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'academics': page_obj,
        'query' : query,
    }

    return render(request, 'academic/index.html', context)

def create_academic(request):
    courses = Course.objects.all()
    years = Year.objects.all()

    context = {
    'courses': courses,
    'years': years
    }

    return render(request, 'academic/create.html', context)

def store_academic(request):
    courseid = request.POST.get('course_id')
    yearid = request.POST.get('year_id')
    unit = request.POST.get('unit')
    schoolyear = request.POST.get('school_year')

    Academic.objects.create(course_id = courseid, year_id= yearid, unit = unit, school_year=schoolyear)

    messages.success(request, 'Academic succesfully saved.')

    return redirect('/students')

def show_academic(request, student_id):
    course = Course.objects.all()
    year = Year.objects.all()
    academic = Academic.objects.get(pk=student_id)

    context = {
        'academic': academic,
        'course': course,
        'year': year,
    }

    return render(request, 'academic/show.html', context)

def edit_academic(request, student_id):
    course = Course.objects.all()
    year = Year.objects.all()
    academic = Academic.objects.get(pk=student_id)

    context = {
        'academic': academic,
        'course': course,
        'year': year,
    }

    return render(request, 'academic/show.html', context)

def update_academic(request, student_id):
    unit = request.POST.get('unit')
    courseid = request.POST.get('course_id')
    yearid = request.POST.get('year_id')
    unit = request.POST.get('unit')
    schoolyear = request.POST.get('school_year')

    Academic.objects.filter(pk=student_id).update( course_id = courseid, year_id= yearid, unit = unit, school_year = schoolyear)

    messages.success(request, 'Academic succesfully Update.')

    return redirect('/academics')

def delete_academic(request, student_id):
    academic = Academic.objects.get(pk=student_id) 

    context = {
        'academic': academic,
    }

    return render(request, 'academic/delete.html', context)

def destroy_academic(request, student_id):
    Academic.objects.filter(pk=student_id).delete()
    messages.success(request, 'Academic successfully deleted.')

    return redirect('/academics')