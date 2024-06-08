from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Profile_Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)

    #gender    
    GENDER_M = "male"
    GENDER_F = "female"
    GENDER_CHOICES = (
    	(GENDER_M, "Male"),
        (GENDER_F, "Female"),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=False)

    birth = models.DateField(blank=False, null=False)
    
    department = models.CharField(max_length=20, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=50, blank=False)
    certification = models.FileField(upload_to="student_certification/")
    #scraped = models.ManyToManyField()

class Profile_Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)
    email = models.CharField(max_length=50, blank=False)
    certification = models.FileField(upload_to="staff_certification/")