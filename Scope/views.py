from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
import random
from .models import Student
from .models import Course
from .models import Review
from .models import Misc
from .forms import student_Form
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import logout
from .forms import student_Form 
from .forms import ProfileEditForm




# Create your views here.

def home(request):
     courses = Course.objects.all()
     images = Misc.objects.all()
     return render(request,'index.html',{'courses':courses ,'images':images})

def about(request):
     images = Misc.objects.all()
     return render(request,'about.html',{'images':images})

def course(request,):
     courses = Course.objects.all()
     images = Misc.objects.all()
     return render(request,['course.html','common.html'],{'courses':courses ,'images':images}) 

def course_detail(request,course_name):
     course = get_object_or_404(Course, Name__iexact=course_name)
     images = Misc.objects.all()
     return render(request, 'course_detail.html', {'course': course ,'images':images})   
           
def feature(request):
     images = Misc.objects.all()
     return render(request,'feature.html',{'images':images})

def testimonial(request):
     review = Review.objects.all()
     images = Misc.objects.all()
     return render(request,'testimonial.html',{'review':review ,'images':images})

def privacy(request):
     images = Misc.objects.all()
     return render(request,'privacy.html',{'images':images})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('sender_Name')
        email = request.POST.get('sender_Mail')
        subject = request.POST.get('mail_Sub')
        message = request.POST.get('sender_Text')

        full_message = f"From: {name} <{email}>\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                email,  # From email (user's email)
                ['aparnaanil573@gmail.com'],  # To email (your support email)
                fail_silently=False,
                
            )
            return render(request, 'success_Mail.html')
        except Exception as e:
            return render(f"An error occurred: {e}")
    
    
    images = Misc.objects.all()
    return render(request, 'contact.html',{'images':images})  # Replace with your actual template


def admission(request):
     if request.method=='POST':
          stuForm = student_Form(request.POST)
          if stuForm.is_valid():
               full_Name = request.POST['full_name']
               DateofBirth = request.POST['dob']   
               gender = request.POST['gender'] 
               email  = request.POST['email'] 
               mob = request.POST['mob'] 
               education = request.POST['education'] 
               guard_name = request.POST['guardian'] 
               guard_occu = request.POST['guard_occupation'] 
               guard_mob = request.POST['guard_mob'] 
               course = request.POST['course'] 
               mode = request.POST['mode'] 
               location = request.POST['location'] 
               timing = request.POST['timing'] 
               address = request.POST['address'] 
               country = request.POST['country'] 
               state = request.POST['state'] 
               city = request.POST['city'] 
               pin_code = request.POST['pin'] 
               
               new_Student = Student(
                    Full_Name = full_Name,
                    Date_of_Birth = DateofBirth,
                    Gender = gender,
                    Email = email,
                    Mobile_number = mob,
                    Education_Qualification  = education,
                    Guardian_Name = guard_name,
                    Guardian_Occupation = guard_occu,
                    Guardian_Mobile = guard_mob,
                    Course  = course,
                    Training_Mode = mode,
                    Location = location,
                    Preferred_Timings = timing,
                    Address = address,
                    Country = country,
                    State = state,
                    City = city,
                    Pin_code = pin_code
               )
               new_Student.save()
               
            

            #    # Send email to the student
            #    send_mail(
            #    subject="Your Course Portal Login Password",
            #    message=f"Dear {full_Name},\n\nYour account has been created.\nTemporary Password:{password}\nPlease log in and change your password immediately.",
            #    from_email="aparnaanil573@gmail.com",  # Replace with your email
            #    recipient_list=[email],
            #    fail_silently=False,
            #    )
               return  render(request, 'success_Form.html')

          else:
               return render(request, 'index1.html',{"formError":stuForm})
          
     return render(request, 'index1.html')




def generate_passcode(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()

        student_qs = Student.objects.filter(Email__iexact=email)
        if not student_qs.exists():
            return HttpResponse("This email is not registered. Please contact admin.")
        
        student = student_qs.first()

        temp_passcode = str(random.randint(100000, 999999))

        student.Password = make_password(temp_passcode)
        student.Is_First_Login = True
        student.save()

        send_mail(
            subject="Your Temporary Passcode",
            message=f"Hi {student.Full_Name},\n\nHere is your 6-digit temporary passcode: {temp_passcode}\nPlease log in and change your password immediately.",
            from_email="your@email.com",
            recipient_list=[email],
            fail_silently=False,
        )

        return  render(request, 'success_Dashmail.html')

    return render(request, 'generate_passcode.html')

# def stu_Login(request):
#     if request.method == 'POST':
#      email = request.POST.get('email')
#      password = request.POST.get('password')
#      user = authenticate(username=email, password=password)
#      if user:
#           login(request, user)
#           student = Student.objects.get(user=user)
#           if student.Is_First_Login:
#             return redirect('force_password_change')
#           return redirect('student_dashboard')
#      else:
#           return HttpResponse("Invalid login credentials")
#     return render(request, 'student_Login.html')

def stu_Login(request):
    images = Misc.objects.all()

    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password')
        
        student = Student.objects.filter(Email__iexact=email).first()
        if student and check_password(password, student.Password):
            request.session['student_id'] = student.id  # Manually log them in
            if student.Is_First_Login:
                return redirect('force_password_change')
            return redirect('student_dashboard')
        else:
            return render(request, 'fail_Login.html')
        
    return render(request, 'student_Login.html',{'images':images})
# def stu_Login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email', '').strip().lower()
#         password = request.POST.get('password')

#         student = Student.objects.filter(Email__iexact=email).first()
#         if student:
#             # Debug prints
#             print("Password entered:", password)
#             print("Hashed in DB:", student.Password)
#             print("Match:", check_password(password, student.Password))

#         if student and check_password(password, student.Password):
#             request.session['student_id'] = student.id  # Manually log them in
#             if student.Is_First_Login:
#                 return redirect('force_password_change')
#             return redirect('student_dashboard')
#         else:
#             return HttpResponse("Invalid login credentials.")
#     return render(request, 'student_Login.html')


#Password Change View

# @login_required
# def force_password_change(request):
#     if request.method == 'POST':
#      form = SetPasswordForm(user=request.user, data=request.POST)
#      if form.is_valid():
#           form.save()
#           update_session_auth_hash(request, request.user)
#           student = Student.objects.get(user=request.user)
#           student.Is_First_Login = False
#           student.save()
#           return redirect('student_dashboard')
#     else:
#         form = SetPasswordForm(user=request.user)
#     return render(request, 'force_password_change.html', {'form': form})

# def force_password_change(request):
#     if request.method == 'POST':
#         form = SetPasswordForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, request.user)

#             student = Student.objects.filter(user=request.user).first()
#             if student:
#                 student.Is_First_Login = False
#                 student.save()

#             return redirect('student_dashboard')
#     else:
#         form = SetPasswordForm(user=request.user)

#     return render(request, 'force_password_change.html', {'form': form})


def force_password_change(request):
    # 🔒 Ensure student is logged in
    if 'student_id' not in request.session:
        return redirect('stu_Login')

    student_id = request.session['student_id']
    student = Student.objects.filter(id=student_id).first()
    if not student:
        return HttpResponse("Student record not found.")

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            return HttpResponse("Passwords do not match.")
        if len(new_password) < 8:
            return HttpResponse("Password must be at least 8 characters.")

        student.Password = make_password(new_password)
        student.Is_First_Login = False
        student.save()

        return redirect('student_dashboard')

    return render(request, 'force_password_change.html')



def student_dashboard(request):
    images = Misc.objects.all()
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('stu_Login')

    student = Student.objects.filter(id=student_id).first()
    if not student:
        return HttpResponse("Student record not found.")
    
    if not student.Profile_Image:
        messages.warning(request, "Please upload your profile image.")
        return redirect('student_profile')  # force them to complete profile
    
    course = None
    if student.Course:
     course = Course.objects.filter(Name__iexact=student.Course.strip()).first()

    return render(request, 'student_dashboard.html', {
        'student': student,
        'course': course,
        'images': images
        # send matched course
    })
    
# def dashboard_courses(request):
#     student_id = request.session.get('student_id')
#     if not student_id:
#         return redirect('stu_Login')

#     student = Student.objects.filter(id=student_id).first()
#     if not student:
#         return HttpResponse("Student record not found.")
#     course = Course.objects.filter(Name__icontains=student.Course.strip()).first()
#     courses = Course.objects.all()
#     return render(request, 'dash_courses.html', {'student': student,'course': course ,'courses':courses})
    
    
def dashboard_courses(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('stu_Login')

    student = Student.objects.filter(id=student_id).first()
    if not student:
        return HttpResponse("Student record not found.")

    course = None
    if student.Course:
        course = Course.objects.filter(Name__iexact=student.Course.strip()).first()
    # (Name__iexact=student.Course.strip()).first()
    courses = Course.objects.all()

    if request.method == "POST":
        course_name = request.POST.get("course_name")
        selected_course = Course.objects.filter(Name__iexact=course_name.strip()).first()

        if selected_course:
            # Prevent duplicates
            if not student.Additional_Courses_Chosen.filter(id=selected_course.id).exists():
                student.Additional_Courses_Chosen.add(selected_course)

            return render(request, 'success_dash.html')

    return render(request, 'dash_Courses.html', {
        'student': student,
        'course': course,
        'courses': courses
    })
    
    

def student_profile(request):
    student_id = request.session.get('student_id')
    student = Student.objects.filter(id=student_id).first()
    if not student:
        return HttpResponse("Student not found.")

    course = None
    if student.Course:
        course = Course.objects.filter(Name__iexact=student.Course.strip()).first()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            updated_student = form.save(commit=False)
            password_input = form.cleaned_data.get('Password')
            if password_input:
                from django.contrib.auth.hashers import make_password
                updated_student.Password = make_password(password_input)
            else:
                updated_student.Password = student.Password  # retain old one
            updated_student.save()
            messages.success(request, "Profile updated.")
            return redirect('student_profile')
    else:
        form = ProfileEditForm(instance=student)

    return render(request, 'dash_Profile.html', {
        'form': form,
        'student': student,
        'course': course
    })



def stu_logout(request):
    logout(request)  # Clears session safely and regenerates CSRF

# Optionally, also:
    request.session.cycle_key()  # Clears session including student_id
    return redirect('stu_Login')  # Redirect to login page


     
     
     
     
     
     
     
     
  







