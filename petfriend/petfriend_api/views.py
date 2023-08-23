from django.shortcuts import render
from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        print("Can't see JSON")
    data["message"] = "This is API test"
    data["headers"] = dict(request.headers)
    print(data)
    return JsonResponse(data)
