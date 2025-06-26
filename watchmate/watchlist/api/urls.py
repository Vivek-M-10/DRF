from django.urls import path
from watchlist.api import views

urlpatterns = [
    path('list/', views.movie_list, name='movie-list'),
    path('detail/<int:pk>/', views.movie_detail, name='movie-detail'),
]