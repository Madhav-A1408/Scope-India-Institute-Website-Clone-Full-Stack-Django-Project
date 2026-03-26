from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('course/',views.course, name="course"),
    path('courses/<str:course_name>/',views.course_detail,name='course_detail'),
    path('feature/',views.feature, name="feature"),
    path('testimonial/',views.testimonial, name="testimonial"),
    path('contact/',views.contact, name="contact"),
    path('admission/',views.admission, name="admission"),
    path('privacy/',views.privacy, name = 'privacy'),
    path('stu_Login/',views.stu_Login, name = 'stu_Login'),
    path('generate-passcode/', views.generate_passcode, name='generate_passcode'),
    path('force_password_change/', views.force_password_change, name='force_password_change'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('dashboard_Course/', views.dashboard_courses, name='dashboard_courses'),
    path('dashboard/profile/', views.student_profile, name='student_profile'),
    path('stu_logout/', views.stu_logout, name='stu_logout'),
    
    
    
   
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
