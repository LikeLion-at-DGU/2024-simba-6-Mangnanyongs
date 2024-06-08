from django.contrib import admin
from .models import Profile_Staff, Profile_Student

# Register your models here.
admin.site.register(Profile_Student)
admin.site.register(Profile_Staff)