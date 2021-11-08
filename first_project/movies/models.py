from django.db import models
from django.db.models import fields

# Create your models here.

class Movie(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField('Movie Name',max_length=255)
    description = models.TextField('Movie Description')
    likes = models.ImageField(default=0)
    watch_count = models.IntegerField(default=0)
    rate = models.PositiveSmallIntegerField(default=0)
    production_date = models.DateTimeField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name