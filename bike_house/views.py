import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import *
from .helper import json_body
from .forms import *


# Create your views here.

# Show place list
def place_list(request):
    bike_place = {'bike_place': list(Place.objects.values())}
    return JsonResponse(bike_place, status=200, safe=False)


# Add Place
@csrf_exempt
@require_http_methods(["POST"])
def add_place(request):
    # getting api data
    user_place = FormPlaceAdd(json_body(request))

    # validation
    if user_place.is_valid():
        user_place.save()
        return JsonResponse({'message': 'place added'}, status=201, safe=False)
    else:
        return JsonResponse({'message': user_place.errors}, status=422)


# Add BikeHouse
@csrf_exempt
@require_http_methods(["POST"])
def add_bike(request):
    # json api data
    payload = json_body(request)
    place = payload['place']
    bike = payload['bike']
    place_obj = Place.objects.create(**place)
    print(bike)
    bike.update({'place':place_obj})
    print(bike)
    user_bike = FormBikeAdd(bike)
    # user_bike = FormBikeAdd(json_body(request))

    # validation
    if user_bike.is_valid():
        user_bike.save()
        return JsonResponse({'message': 'Bike Added'}, status=201, safe=False)
    else:
        return JsonResponse({'message': user_bike.errors}, status=422)
