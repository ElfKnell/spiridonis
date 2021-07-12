from django.urls import path
from .views import CustomUserListView, CustomUserDetailView


urlpatterns = [
    path('all/', CustomUserListView.as_view()),
    path('detail/<int:pk>', CustomUserDetailView.as_view())
]