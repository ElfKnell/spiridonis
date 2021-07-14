from django.urls import path
from .views import AttributesValueCreateView, AttributesCreateView, AttributesValueListView
from .views import AttributesListView, AttributesValueDetailView, AttributesDetailView


app_name = 'Attributes'
urlpatterns = [
    path('create/', AttributesCreateView.as_view()),
    path('all/', AttributesListView.as_view()),
    path('detail/<int:pk>', AttributesDetailView.as_view()),
    path('value/create/', AttributesValueCreateView.as_view()),
    path('value/all', AttributesValueListView.as_view()),
    path('value/detail/<int:pk>', AttributesValueDetailView.as_view())
]
