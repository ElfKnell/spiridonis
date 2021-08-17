from django.urls import path
from .views import SetCreateView, SetListView, SetDetailView


app_name = 'Set'
urlpatterns = [
    path('create/', SetCreateView.as_view()),
    path('all', SetListView.as_view()),
    path('detail/<str:slug>', SetDetailView.as_view())
]
