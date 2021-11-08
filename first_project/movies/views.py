from django.shortcuts import redirect, render
from movies.models import Movie

# Create your views here.
def movie_index(req):
    all_movies = Movie.objects.all()
    return render(req,'movies/movie_index.html',context={'movies': all_movies})

def movie_detail(req,pk):
    movie = Movie.objects.get(pk=pk)
    return render(req,'movies/movie_detail.html',context={'movie':movie})

def movie_create(req):
    if  req.method == 'POST':
        movie_name = req.POST.get('name')
        movie_desc = req.POST.get('desc')
        movie_likes = req.POST.get('likes')
        movie_data = {
            'name':movie_name,
            'description':movie_desc,
            'likes':movie_likes
        }
        return redirect('movie:movie_index')
    return render(req,'movies/movie_create.html')

def movie_delete(req, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movie:movie-index')

def movie_update(req):
    pass