from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics

from .permissions import IsOwnerOrReadOnly

from .serializers import PetSerializer, PetDetailSerializer

from django.forms.models import model_to_dict
import json

from .models import *

#Not a part of actual api. It's just test View for practising manual requests and testing dockerized api
def api_home_manual(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        print("Can't see JSON")
    data["message"] = "This is API test"
    data["headers"] = dict(request.headers)
    data["param"] = dict(request.GET)
    print(data)
    return JsonResponse(data)

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    data = {}
    if request.method == 'GET':
        instance = Pet.objects.all().order_by("?").first()
        if instance:
            data = PetSerializer(instance).data
        return Response(data)
    elif request.method == 'POST':
        query = request.data
        try:
            instance = Pet.objects.get(pk=query['id'])
            data = PetSerializer(instance).data
        except:
            data = json.dumps({"message": "There is no such a pet"})
        return Response(data)
    
@api_view(["POST"])
def add_pet(request, *args, **kwargs):
    serializer = PetSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response({"valid data": f"created new pet {instance.name}"})
    return Response({"invalid data": "couldn't create new pet"}, status=400)

class PetView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all pets for given requested user
        '''
        print(request)
        pets = Pet.objects.filter(user = request.user.petfrienduser)
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PetDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get_object(self, pet_id, user):
        '''
        Helper method to get the object with given pet_id and user_id
        '''
        try:
            return Pet.objects.get(id=pet_id, user = user)
        except Pet.DoesNotExist:
            return None
    def get(self, request, pet_id, *args, **kwargs):
        '''
        Retrieves the Pet with given todo_id
        '''
        pet = self.get_object(pet_id, request.user.petfrienduser)
        if not pet:
            return Response(
                {"res": "Object with pet id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PetDetailSerializer(pet)
        return Response(serializer.data, status=status.HTTP_200_OK)   
    def put(self, request, pet_id, *args, **kwargs):
        '''
        Updates pet with given id if exists
        '''
        pet = self.get_object(pet_id, request.user.id)
        if not pet:
            return Response(
                {"res": "Object with pet id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = PetDetailSerializer(instance = pet, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pet_id, *args, **kwargs):
        '''
        Deletes the pet with given pet_id if exists
        '''
        pet = self.get_object(pet_id, request.user.petfrienduser)
        if not pet:
            return Response(
                {"res": "Object with pet id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        pet.delete()
        return Response(
            {"res": "Pet object deleted!"},
            status=status.HTTP_200_OK
        )

class PetCreateAPIView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetDetailSerializer

    def perform_create(self, serializer):
        sex = serializer.validated_data.get('sex')
        name = serializer.validated_data.get('name') or None
        if name is None and sex == 1:
            name = "John Doe"
        elif name is None and sex == 2:
            name = "Jane Doe"
        serializer.save(user=self.request.user.petfrienduser, name=name)
        # send a Django signal here
