from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    #User, Profile 생성 후 writer부분 수정 예정
    #writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    building = models.ImageField(upload_to="post/", blank=True, null=True)
    organization = models.CharField(max_length=50, null=True)
    
    writer = models.CharField(max_length=50)
    
    department = models.CharField(max_length=50, null=True)
    is_income_bracket = models.PositiveIntegerField(null=False, default=0) #boolean
    is_attending = models.PositiveIntegerField(null=False, default=0) #boolean
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    deadline = models.DateField(null=True)
    day_left = models.IntegerField(null=True)#남은날짜
    place = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=50, blank=False)
    time = models.TextField(max_length=50, null=False)
    recruitment = models.PositiveIntegerField(null=True, default=0)
    wage = models.PositiveIntegerField(null=True, default=0)
    body = models.TextField()
    file = models.ImageField(upload_to="post/", blank=True, null=True)
    pub_date = models.DateTimeField()
    scrap = models.ManyToManyField(User, related_name='scraped', blank=True, null=True, default=None)
    scrap_count = models.PositiveIntegerField(default=0)
    inquiry = models.PositiveIntegerField(default=0)
    applicated_count = models.PositiveIntegerField(default=0)