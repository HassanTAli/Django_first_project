from django.shortcuts import redirect, render
from movies.models import Movie
from movies.form import MovieForm

# Create your views here.


def movie_index(req):
    all_movies = Movie.objects.all()
    return render(req, 'movies/movie_index.html', context={'movies': all_movies})


def movie_detail(req, pk):
    movie = Movie.objects.get(pk=pk)
    
    # movie.casts.all() -> Access many2many for the casts
    # movie.review_set.all() -> Access Foreign Key relation for the related reviews
    
    return render(req, 'movies/movie_detail.html', context={'movie': movie})

# def movie_create(req):
#     if  req.method == 'POST':
#         movie_name = req.POST.get('name')
#         movie_desc = req.POST.get('desc')
#         movie_likes = req.POST.get('likes')

#         movie_object = Movie.objects.create(
#             name=movie_name,
#             description=movie_desc,
#             likes=movie_likes,
#             active=True
#         )
#         return redirect('movie:movie_index')
#     return render(req,'movies/movie_create.html')


def movie_create(req):
    form = MovieForm()
    if req.method == 'POST':
        form = MovieForm(data=req.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:movie_index')
    return render(req, 'movies/movie_create.html', context={'form': form})


def movie_delete(req, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movie:movie_index')


def movie_update(req, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if req.method == 'POST':
        form = MovieForm(data=req.POST,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:movie-detail', pk=movie.id)
    
    return render(req, 'movies/movie_update.html', context={'form': form,'movie':movie})
