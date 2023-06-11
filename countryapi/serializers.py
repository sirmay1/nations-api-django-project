from .models import World
from rest_framework import serializers


class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ('id', 'name', 'continent', 'language', 'ethnicity')
