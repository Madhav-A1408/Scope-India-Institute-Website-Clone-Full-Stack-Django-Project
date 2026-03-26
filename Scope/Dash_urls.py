from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

   
    path('home/', views.student_dashboard, name='student_dashboard'),  # main dashboard
    path('courses/', views.dashboard_courses, name='dashboard_courses'),
    path('analytics/', views.dashboard_analytics, name='dashboard_analytics'),
    # add more as needed

    
    
    
    
   
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)