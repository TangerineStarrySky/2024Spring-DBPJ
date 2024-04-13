from django.urls import path
from cinema.views import *

urlpatterns = [
    path('', welcome, name='welcome'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('movies/', show_movies, name='movies'),
    path('movieinfo/<int:movie_id>/', show_movie_info, name='movieinfo'),
    path('addmovies/', add_movies, name='addmovies'),

    path('handle_registration/', handle_registration, name='handle_registration'),
    path('handle_login/', handle_login, name='handle_login'),
]