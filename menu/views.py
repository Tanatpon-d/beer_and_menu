from rest_framework.response import Response
from menu.models import Menu, MenuItem
from menu.serializers import MenuItemSerializer, MenuSerializer
from rest_framework import generics
from rest_framework import viewsets


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def list(self, request, *args, **kwargs):
        # Get all menu items
        menus = Menu.objects.all()

        # Define the desired response structure
        response_data = {
            "status": True,
            "code": 200,
            "data": MenuSerializer(menus, many=True).data
        }
        return Response(response_data)


class MenuRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItem
