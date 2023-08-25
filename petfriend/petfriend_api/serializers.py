from rest_framework import serializers


from .models import *

class PetSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Pet
        fields = [
            'id',
            'name',
            'genre',
            'species',
            'variety',
            'user',
            'age'
        ]
    def get_age(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Pet):
            return None
        return obj.get_age()

class FullPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
