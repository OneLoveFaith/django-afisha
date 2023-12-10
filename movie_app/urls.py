from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DirectorsViewSet, MoviesViewSet, ReviewsViewSet

default_router = DefaultRouter()
default_router.register('directors', DirectorsViewSet, basename='director')
default_router.register('reviews', ReviewsViewSet, basename='review')
default_router.register('movies', MoviesViewSet, basename='movie')


urlpatterns = [
    # path('movies/', MovieList.as_view(), name='movie-list'),
    # path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    # path('movies/reviews/', MovieReviewsList.as_view(), name='movie-reviews-list'),
    # path('reviews/', ReviewList.as_view(), name='review-list'),
    # path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

]

urlpatterns += default_router.urls