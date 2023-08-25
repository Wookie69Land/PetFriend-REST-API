from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PetSerializer

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
        print(instance)
        return Response({"valid data": f"created new pet {instance.name}"})
    return Response({"invalid data": "couldn't create new pet"}, status=400)