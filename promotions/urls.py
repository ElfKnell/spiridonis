from django.urls import path
from .views import PromotionsListView, PromotionsCreateView, PromotionsDetail


app_mane = 'Promotions'
urlpatterns = [
    path('create/', PromotionsCreateView.as_view()),
    path('all', PromotionsListView.as_view()),
    path('detail/<str:slug>', PromotionsDetail.as_view())
]
