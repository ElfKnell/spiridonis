from django.urls import path
from .views import NewsCreateView, NewsListView, NewsDetailView


app_name = 'news'
urlpatterns = [
    path('create/', NewsCreateView.as_view()),
    path('all/', NewsListView.as_view()),
    path('detail/<int:pk>', NewsDetailView.as_view())
]
