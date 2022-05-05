from rest_framework import serializers

from .models import Disc, Rubber


class DiscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disc
        fields = ('brand', 'diametr')


class RubberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubber
        fields = ('brand', 'width', 'profile', 'diametr')
