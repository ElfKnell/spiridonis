from django.urls import path
from .views import RatingCreateView, RatingStarCreateView, RatingStarListView, \
        RatingStarDetailView, RatingListView


app_name = 'rating'
urlpatterns = [
    path('star/create', RatingStarCreateView.as_view()),
    path('star/all', RatingStarListView.as_view()),
    path('star/detail/<int:pk>', RatingStarDetailView.as_view()),
    path('create', RatingCreateView.as_view()),
    path('all', RatingListView.as_view())
]
