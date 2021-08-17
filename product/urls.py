from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView


app_name = 'product'
urlpatterns = [
    path('create/', ProductCreateView.as_view()),
    path('all', ProductListView.as_view()),
    path('detail/<str:slug>', ProductDetailView.as_view())
]
