from .views import BasketListView, BasketCreateView, BasketDetailView, \
    OrderCreateView, OrderListView, OrderDetailView, SelectionCreateView, \
    SelectionListView, SelectionDetailView
from django.urls import path

app_name = 'basket'
urlpatterns = [
    path('create', BasketCreateView.as_view()),
    path('all', BasketListView.as_view()),
    path('detail/<int:pk>', BasketDetailView.as_view()),
    path('order/create', OrderCreateView.as_view()),
    path('order/all', OrderListView.as_view()),
    path('order/detail/<int:pk>', OrderDetailView.as_view()),
    path('selection/create', SelectionCreateView.as_view()),
    path('selection/all', SelectionListView.as_view()),
    path('selection/detail/<int:pk>', SelectionDetailView.as_view())
]
