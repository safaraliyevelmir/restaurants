from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializers

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializers

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        radius = self.request.query_params.get('radius')
        lat = self.request.query_params.get('lat')
        lng = self.request.query_params.get('lng')

        if radius and lat and lng:
            min_lat = float(lat) - float(radius)
            max_lat = float(lat) + float(radius)
            min_lng = float(lng) - float(radius)
            max_lng = float(lng) + float(radius)

            queryset = queryset.filter(latitude__gte=min_lat, latitude__lte=max_lat, longitude__gte=min_lng, longitude__lte=max_lng)

        return queryset
    

""""
    {
        "id": 1,
        "fire_id": "blabla",
        "nane": "Bla",
        "latitude": 41.5,
        "longitude": -87.5
    }

"""