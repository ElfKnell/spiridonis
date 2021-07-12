from django.urls import path
from .views import CompanyCreateView, CompanyListView, CompanyDetailView


app_name = 'Company'
urlpatterns = [
    path('create/', CompanyCreateView.as_view()),
    path('all', CompanyListView.as_view()),
    path('detail/<int:pk>', CompanyDetailView.as_view())
]
