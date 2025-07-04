from django.urls import path
from watchlist.api import views

urlpatterns = [
    path('list/', views.WatchlistView.as_view(), name='movie-list'),
    path('detail/<int:pk>/', views.WatchlistDetailView.as_view(), name='movie-detail'),
    path('platforms/', views.StreamPlatformView.as_view(), name='platform-list'),
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
]


