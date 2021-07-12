from django.urls import path
from .views import ManufacturerCreateView, ManufacturerListView, ManufacturerDetailView


app_name = 'Manufacturer'
urlpatterns = [
    path('create/', ManufacturerCreateView.as_view()),
    path('all/', ManufacturerListView.as_view()),
    path('detail/<int:pk>', ManufacturerDetailView.as_view())
]
