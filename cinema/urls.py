from django.urls import path
from cinema.views import *

urlpatterns = [
    path('', welcome, name='welcome'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),

    path('addmovies/', add_movies, name='addmovies'),

    path('handle_registration/', handle_registration, name='handle_registration'),
    path('handle_login/', handle_login, name='handle_login'),

    path('history/<int:user_id>', history, name='history'),


    path('movies/<int:user_id>/', show_movies, name='movies'),
    path('movieinfo/<int:user_id>/<int:movie_id>/', show_movie_info, name='movieinfo'),
    path('rooms/<int:user_id>/<int:movie_id>/', show_rooms, name='rooms'),
    path('buy/<int:user_id>/<int:movie_id>/<int:room_id>/', buy, name='buy'),
    path('confirm_purchase/<int:ticket_id>/', confirm_purchase, name='confirm_purchase'),



    path('valuation/<int:ticket_id>/', valuation, name='valuation'),
    path('submit_rating/<int:ticket_id>', submit_rating, name='submit_rating'),

]