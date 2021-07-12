from django.urls import path
from .views import VProductCreateView, VProductListView, VProductDetailView


app_name = 'Variability product'
urlpatterns = [
    path('create/', VProductCreateView.as_view()),
    path('all/', VProductListView.as_view()),
    path('detail/<int:pk>', VProductDetailView.as_view())
]
