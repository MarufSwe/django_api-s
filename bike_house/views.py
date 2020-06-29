import json

from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404
# from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import *
from .helper import json_body
from .forms import *


# Create your views here.

# Show place list
def place_list(request):
    bike_place = {'place': list(Place.objects.values())}
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


@csrf_exempt
@require_http_methods(["POST"])
def update_place(request, id=id):
    # catch the editable id (object)
    edit_place = Place.objects.get(id=id)

    # getting api data
    form = FormPlaceEdit(json_body(request), instance=edit_place)

    # validation
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'place updated'}, status=201)
    else:
        return JsonResponse({'message': form.errors}, status=422)



# # Update Place
# @method_decorator(csrf_exempt, name='dispatch')
# class UpdatePlace(View):
#     def put(self, request, id=id):
#
#         # catch the editable id (object)
#         place_object = Place.objects.get(id=id)
#
#         # getting api data
#         form = FormPlaceEdit(json_body(request), instance=place_object)
#
#         # validation
#         if form.is_valid():
#             form.save()
#             return JsonResponse({"message": "Place Successfully Updated"}, status=201, safe=False)
#         else:
#             return JsonResponse({"message": form.errors}, status=422)



# delete Place
@csrf_exempt
def delete_place(request, id):
    place = get_object_or_404(Place, id=id)
    if request.method == "POST":
        place.delete()
        return JsonResponse({'message': 'place deleted'}, status=204)
    else:
        return JsonResponse({'message': place.errors}, status=422)


# ==================================Bike==========================================

# Show bike list
def bike_list(request):
    bike_list = {'bike_list': list(BikeHouse.objects.values())}
    return JsonResponse(bike_list, status=200, safe=False)


# Add Bike
@csrf_exempt
@require_http_methods(["POST"])
def add_bike(request):
    # # json api data
    # payload = json_body(request)
    # place = payload['place']
    # bike = payload['bike']
    # place_obj = Place.objects.create(**place)
    # print(bike)
    # bike.update({'place':place_obj})
    # print(bike)
    # user_bike = FormBikeAdd(bike)
    user_bike = FormBikeAdd(json_body(request))

    # validation
    if user_bike.is_valid():
        user_bike.save()
        return JsonResponse({'message': 'Bike Added'}, status=201, safe=False)
    else:
        return JsonResponse({'message': user_bike.errors}, status=422)


# delete bike
@csrf_exempt
def delete_bike(request, id):
    bike = get_object_or_404(BikeHouse, id=id)
    if request.method == "POST":
        bike.delete()
        return JsonResponse({'massage': 'delete bike successfully'}, status=204)
    else:
        return JsonResponse({'massage': bike.errors}, status=422)


# ==================================Customer=============================

# show customer list
def customer_list(request):
    customer = {'customer_list': list(Customer.objects.values())}
    return JsonResponse(customer, status=201)


# add customer
@csrf_exempt
@require_http_methods(["POST"])
def add_customer(request):
    # getting api data
    customer = FormCustomer(json_body(request))

    # validation
    if customer.is_valid():
        customer.save()
        return JsonResponse({'message': 'customer added'}, status=204)
    else:
        return JsonResponse({'message': customer.errors}, status=422)
