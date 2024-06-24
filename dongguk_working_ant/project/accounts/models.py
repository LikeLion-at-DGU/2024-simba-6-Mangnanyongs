from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Profile(models.Model):
    student_or_staff = models.CharField(max_length=20, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=5, blank=False)

    #gender    
    GENDER_M = "male"
    GENDER_F = "female"
    GENDER_CHOICES = (
    	(GENDER_M, "Male"),
        (GENDER_F, "Female"),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)

    birth = models.DateField(blank=False, null=True)
    
    photo = models.ImageField(upload_to="user_photo/", blank=True)
    department = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=False)
    student_number = models.CharField(max_length=10, blank=False)
    income = models.PositiveIntegerField(null=True, default=0)
    certification_student = models.FileField(upload_to="student_certification/", blank=True)
    certification_staff = models.FileField(upload_to="staff_certification/",blank=True)
    #scraped = models.ManyToManyField()

class Notice(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=20, blank=True)
    link = models.CharField(max_length=20, blank=True)
    pub_date = models.DateTimeField()

    def summary(self):
        return self.content[:22]