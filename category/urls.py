from django.urls import path
from .views import CategoryCreateView, CategoryListView, CategoryDetailView


app_name = 'category'
urlpatterns = [
    path('create/', CategoryCreateView.as_view()),
    path('all/', CategoryListView.as_view()),
    path('detail/<str:slug>', CategoryDetailView.as_view()),
]