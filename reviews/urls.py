from django.urls import path
from .views import ReviewsCreateView, ReviewsListView, ReviewsDetailView


app_name = 'Reviews'
urlpatterns = [
    path('create/', ReviewsCreateView.as_view()),
    path('all', ReviewsListView.as_view()),
    path('detail/<int:pk>', ReviewsDetailView.as_view())
]
