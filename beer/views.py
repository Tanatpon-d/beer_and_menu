# beer_app/views.py

# from urllib import response
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Beer
from .serializers import BeerSerializer
from mysite.mongo_logger import BeerLogger


def wrap_response(data):
    return {
        "status": True,
        "code": 200,
        "data": data
    }


class BeerListCreateView(generics.ListCreateAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

    def perform_create(self, serializer):
        # Create a new beer
        serializer.save()

        # Log the creation action
        logger = BeerLogger()
        logger.log_action('create', serializer.data['name'])
        logger.close()


class BeerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

    def perform_update(self, serializer):
        # Update an existing beer
        serializer.save()

        # Log the update action
        logger = BeerLogger()
        logger.log_action('update', serializer.data['name'])
        logger.close()

    def perform_destroy(self, instance):
        # Delete a beer
        instance.delete()

        # Log the deletion action
        logger = BeerLogger()
        logger.log_action('delete', instance.name)
        logger.close()


