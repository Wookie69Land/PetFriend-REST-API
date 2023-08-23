from django.shortcuts import render
from django.http import JsonResponse
import json

#Not a part of production. It's just test View for practising manual requests and testing dockerized api
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
