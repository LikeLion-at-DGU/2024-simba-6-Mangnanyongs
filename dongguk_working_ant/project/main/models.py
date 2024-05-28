from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    #User, Profile 생성 후 writer부분 수정 예정
    #writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    organization = models.CharField(max_length=50, null=True)
    
    writer = models.CharField(max_length=50)
    
    department = models.CharField(max_length=50, null=True)
    is_income_bracket = models.IntegerField(null=False) #boolean
    is_attending = models.IntegerField(null=False) #boolean
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    place = models.CharField(max_length=50, null=False)
    content = models.CharField(max_length=50, null=False)
    time = models.TextField(max_length=50, null=False)
    recruitment = models.IntegerField(null=True, default=0)
    wage = models.IntegerField(null=True, default=0)
    body = models.TextField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    pub_date = models.DateTimeField()
    #scrap = models.ManyToManyField(User, related_name='scraped', blank=True)