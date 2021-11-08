from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        # if i want some fields not all ===> fields = ('active','name','description')