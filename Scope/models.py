from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


# Forms 
class Student(models.Model): 
    
    Full_Name = models.CharField(max_length=255,)
    Date_of_Birth = models.DateField()
    Gender = models.CharField(max_length=20)
    Email = models.EmailField()
    Mobile_number = models.CharField(max_length=15)
    Education_Qualification = models.CharField(max_length=255)
    Guardian_Name = models.CharField(max_length=255)
    Guardian_Occupation = models.CharField(max_length=255)
    Guardian_Mobile = models.CharField(max_length=15)
    Course = models.CharField(max_length=255,blank=True)
    Training_Mode = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Preferred_Timings = models.CharField(max_length=100)
    Address = models.TextField()
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Pin_code = models.CharField(max_length=10)
    Student_Created_At = models.DateTimeField(default=timezone.now)
    Is_First_Login = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    Password = models.CharField(max_length=255, blank=True)  # NEW
    Profile_Image = models.ImageField(upload_to='student/',
    null=True,
    blank=True,
    default='student/default.png')  # path inside MEDIA_ROOT)
    Additional_Courses_Chosen = models.ManyToManyField('Course', blank=True,null=True)

    def __str__(self):
        return self.Full_Name
    
    
# Course Display   
class Course(models.Model):
    Title = models.CharField(null=True, blank=True,max_length=255)
    Name= models.CharField(max_length=255,)
    Duration = models.CharField(max_length=50,)
    Timings = models.CharField(max_length=50,)
    Fees = models.CharField(max_length=25,default="₹")
    Batch = models.CharField(max_length=50,)
    Details = models.TextField()
    Overview = models.TextField(blank=True)
    Image_forHome = models.ImageField(upload_to='course/', null=True, blank=True)
    Image_forBanner = models.ImageField(upload_to='course/', null=True, blank=True)
    Image_500x600 = models.ImageField(upload_to='course/', null=True, blank=True)
    Image_80x80 = models.ImageField(upload_to='course/', null=True, blank=True)
    
    def __str__(self):
        return self.Name

    
# Testimonial
class Review(models.Model):
    Name = models.CharField(null=True, blank=True,max_length=255)
    Comments = models.TextField(blank=True)
    Rating = models.CharField(null=True, blank=True)
    Image = models.ImageField()
    
    def __str__(self):
        return self.Name
    
class Misc(models.Model):
    Name = models.CharField(null=True)
    home_Image = models.ImageField()
    feature_Image = models.ImageField()
    rating_Image = models.ImageField(null=True, blank=True)
    certifications_Image = models.ImageField(null=True, blank=True)
    default_Dash = models.ImageField(null=True, blank=True)
    login_page = models.ImageField(null=True, blank=True)
    sign_up_page = models.ImageField(null=True, blank=True)
    
    
    
    def __str__(self):
        return self.Name