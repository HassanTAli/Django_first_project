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
    # banner = models.ImageField()

    def __str__(self) -> str:
        return self.name
    
class Cast(models.Model):
    first_name = models.CharField('Actor Name',max_length=255)