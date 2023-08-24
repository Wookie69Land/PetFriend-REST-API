from rest_framework import serializers


from .models import *

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            'id',
            'name',
            'genre',
            'species',
            'variety',
            'user',
            'get_age'
        ]
