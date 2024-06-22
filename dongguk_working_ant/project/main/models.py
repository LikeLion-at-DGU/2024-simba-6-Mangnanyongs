from django.db import models
import json
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    #User, Profile 생성 후 writer부분 수정 예정
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    organization = models.CharField(max_length=50, null=True)
    
    department = models.CharField(max_length=50, null=True)
    is_income_bracket = models.PositiveIntegerField(null=False, default=0) #boolean
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    deadline = models.DateField(null=True)
    day_left = models.IntegerField(null=True)#남은날짜
    place = models.CharField(max_length=50, blank=False)
    time = models.TextField(max_length=50, null=False)
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
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    is_accepted = models.PositiveIntegerField(null=False, default=0) #boolean


class Answer(models.Model):
    application = models.ForeignKey(Application, null=False, blank=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    file = models.FileField(upload_to="answer_file/", blank=True, null=True)

class Applicated(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    student = models.ManyToManyField(User, related_name='apply', blank=True, default=None)
    is_accepted = models.PositiveIntegerField(null=False, default=0) #boolean

    def __str__(self):
        return 'applicated of ' + str(self.post)