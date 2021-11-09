from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

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
    casts = models.ManyToManyField("Cast")    
    def __str__(self):
        return self.name

class Review(models.Model):
    comment = models.CharField(max_length=50)
    attachment = models.FileField(upload_to='movie/review',null=True,blank=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie",on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return '{} - Review'.format(self.movie)
    
class Cast(models.Model):
    first_name = models.CharField('Actor Name',max_length=255)
    title = models.CharField(max_length=100)
    is_free = models.BooleanField(default=True)
    date_published = models.DateField(null=True,blank=True)
    profile_image = models.ImageField(upload_to='profile/images')
    id_name = models.OneToOneField("ID",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name
    
    #sorting by first-name
    
    class Meta:
        ordering =('first_name',)


class ID(models.Model):
    number=models.CharField(max_length=150)
    
    def __str__(self):
        return self.number
    
class Categories(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    