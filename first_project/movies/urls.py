from django.urls import path
from .views import movie_index,movie_create,movie_detail,movie_update,movie_delete

app_name = 'movie'

urlpatterns = [
    path('movie_index',movie_index,name='movie_index'),
    path('create', movie_create, name='movie_create'),
    path('<int:pk>/detail', movie_detail, name='movie_detail'),
    path('<int:pk>/update', movie_update, name='movie_update'),
    path('<int:pk>/delete', movie_delete, name='movie_delete'),
]
