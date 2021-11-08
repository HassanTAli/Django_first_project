from django.db import models
from django.db.models import fields

# Create your models here.

class Movie(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField('Movie Name',max_length=255)
    description = models.TextField('Movie Description')
    likes = models.IntegerField(default=0)
    watch_count = models.IntegerField(default=0)
    rate = models.PositiveSmallIntegerField(default=0)
    production_date = models.DateField(null=True,blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    banner = models.ImageField(upload_to='movie/images')
    video = models.FileField(upload_to='movie/videos')
    
    def __str__(self):
        return self.name
    
    
class Cast(models.Model):
    first_name = models.CharField('Actor Name',max_length=255)
    title = models.CharField(max_length=100)
    is_free = models.BooleanField(default=True)
    date_published = models.DateField(null=True,blank=True)
    profile_image = models.ImageField(upload_to='profile/images')
    
    def __str__(self):
        return self.first_name
    
    
class Category(models.Model):
    pass