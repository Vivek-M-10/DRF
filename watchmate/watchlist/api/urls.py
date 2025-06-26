from django.urls import path
from watchlist.api import views

urlpatterns = [
    path('list/', views.MovieListView.as_view(), name='movie-list'),
    path('detail/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
]



