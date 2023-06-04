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
            queryset = queryset.filter(
                latitude__range=(float(lat) - float(radius), float(lat) + float(radius)),
                longitude__range=(float(lng) - float(radius), float(lng) + float(radius))
            )

        return queryset
