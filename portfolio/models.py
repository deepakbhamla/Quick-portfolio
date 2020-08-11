from django.db import models
from datetime import datetime
# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=99);
    last_name = models.CharField(max_length=99);
    Bio = models.CharField(max_length=99);
    about_me = models.CharField(max_length=500);
    resume = models.URLField(max_length=200);
    profile_image1 = models.ImageField(upload_to = 'media')
    profile_image2 = models.ImageField(upload_to = 'media')

    def __str__(self):
       return self.first_name



class Contact(models.Model):
    phone= models.CharField(max_length=13);
    email = models.EmailField(max_length=99);
    address = models.CharField(max_length=99);
    instagram = models.URLField(max_length=200);
    github = models.URLField(max_length=200);
    linkedin = models.URLField(max_length=200);

    def __str__(self):
       return self.phone

class Project(models.Model):
    project_name = models.CharField(max_length=99);
    project_category = models.CharField(max_length=99);
    project_link =  models.URLField(max_length=200);
    project_scrnshot = models.ImageField(upload_to = 'media')
    date = models.DateTimeField('default date time', default = datetime.now())

    def __str__(self):
       return self.project_name

class SkillLevel(models.Model):
    skill_name = models.CharField(max_length=99);
    skill_percentage = models.IntegerField(max_length=99);

    def __str__(self):
       return self.skill_name
