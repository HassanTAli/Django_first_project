from django.contrib import admin
from .models import Movie,Cast,Categories,Review,ID

# Register your models here.
admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(Categories)
admin.site.register(Review)
admin.site.register(ID)