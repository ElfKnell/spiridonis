from django.urls import path
from .views import AttributesValueCreateView, AttributesCreateView, AttributesValueListView
from .views import AttributesListView, AttributesValueDetailView, AttributesDetailView
from .views import AttributesVariantCreateView, AttributesVariantListView, AttributesVariantDetailView

app_name = 'Attributes'
urlpatterns = [
    path('create/', AttributesCreateView.as_view()),
    path('all/', AttributesListView.as_view()),
    path('detail/<int:pk>', AttributesDetailView.as_view()),
    path('value/create/', AttributesValueCreateView.as_view()),
    path('value/all', AttributesValueListView.as_view()),
    path('value/detail/<int:pk>', AttributesValueDetailView.as_view()),
    path('variant/create/', AttributesVariantCreateView.as_view()),
    path('variant/all', AttributesVariantListView.as_view()),
    path('variant/detail/<int:pk>', AttributesVariantDetailView.as_view())
]
