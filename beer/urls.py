# beer_app/urls.py

from django.urls import path
from .views import BeerListCreateView, BeerRetrieveUpdateDestroyView

urlpatterns = [
    path('', BeerListCreateView.as_view(), name='beer-list-create'),
    path('<int:pk>/', BeerRetrieveUpdateDestroyView.as_view(), name='beer-detail'),
]
