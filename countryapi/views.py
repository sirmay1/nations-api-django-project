from django.shortcuts import render
from rest_framework import viewsets
from .models import World
from .serializers import WorldSerializer


class WorldView(viewsets.ModelViewSet):
    queryset = World.objects.all()
    serializer_class = WorldSerializer





