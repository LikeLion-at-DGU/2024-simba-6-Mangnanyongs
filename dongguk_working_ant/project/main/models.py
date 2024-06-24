from django.db import models
import json
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    organization = models.CharField(max_length=50, null=True)
    
    department = models.CharField(max_length=50, null=True)
    is_income_bracket = models.PositiveIntegerField(null=False, default=0) #boolean
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    deadline = models.DateField(null=True)
    day_left = models.IntegerField(null=True)
    place = models.CharField(max_length=50, blank=False)
    time = models.TextField(null=False)
    recruitment = models.PositiveIntegerField(default=0)
    wage = models.PositiveIntegerField(null=True, default=0)
    body = models.TextField()

    file = models.ImageField(upload_to="post/", blank=True, null=True)
    pub_date = models.DateTimeField()
    scrap = models.ManyToManyField(User, related_name='scraped', blank=True, default=None)
    scrap_count = models.PositiveIntegerField(default=0)
    applicated_count = models.PositiveIntegerField(default=0)

    #body필드에 TextField를 사용하고 JSON 문자열로 변환하여 저장 > 리스트로 만들어주기 위함
    def set_body(self, body):
        self.body = json.dumps(body)

    def get_body(self):
        return json.loads(self.body)

    def __str__(self):
        return '[' + self.organization + ']' + self.title

class Question(models.Model):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.content + ' from ' + str(self.post)

class Application(models.Model):
    post = models.ForeignKey(Post, null=False, related_name="applications", blank=False, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    is_accepted = models.PositiveIntegerField(null=False, default=0) 
    file = models.FileField(upload_to="application_file/", blank=True, null=True)

class Answer(models.Model):
    application = models.ForeignKey(Application, null=False, blank=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()

class Review(models.Model):
    organization = models.CharField(max_length=50, null=True)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    star = models.PositiveIntegerField(null=False, default=0) #boolean