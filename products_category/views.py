from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import *
from .helper import json_body
from .models import *


# =================================Category====================================

# Show category list
def category_list(request):
    category = {'category_list': list(Category.objects.values())}
    return JsonResponse(category, status=200, safe=False)


# Add Category
@csrf_exempt
@require_http_methods(["POST"])
def add_category(request):
    # getting api data
    # print(request.FILES)
    # print(json_body(request))
    # return JsonResponse({'message': 'false'})
    category = FormCategoryAdd(request.POST, request.FILES)

    # validation
    if category.is_valid():
        category.save()
        return JsonResponse({'message': 'product added'}, status=201, safe=False)
    else:
        return JsonResponse({'message': category.errors}, status=422)


# Update Category
@csrf_exempt
@require_http_methods(["PUT"])
def update_category(request, id):
    # catch the editable id (object)
    category_obj = Category.objects.get(id=id)

    # getting api data from json_body
    form = FormCategoryUpdate(request.POST, request.FILES, instance=category_obj)

    # validation
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'product updated'}, status=201)
    else:
        return JsonResponse({'message': form.errors}, status=422)


# Delete Category
@csrf_exempt
def delete_category(request, id):
    del_category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        del_category.delete()
        return JsonResponse({"message": 'delete category successfully'}, status=204)
    else:
        return JsonResponse({'message': del_category.errors}, status=422)

    # ===============================Product===================================


# Show Product list
def product_list(request):
    product = {'product_list': list(Product.objects.values())}
    return JsonResponse(product, status=200, safe=False)


# Add Product
@csrf_exempt
@require_http_methods(["POST"])
def add_product(request):
    product = FormProductAdd(json_body(request))

    if product.is_valid():
        product.save()
        return JsonResponse({'message': 'product added'}, status=201)
    else:
        return JsonResponse({'message': product.errors})


# Update Product
@csrf_exempt
@require_http_methods(["PUT"])
def update_product(request, id):
    # catch the editable id (object)
    product_obj = Product.objects.get(id=id)

    # getting api data from json_body
    form = FormProductUpdate(json_body(request), instance=product_obj)

    # validation
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'product updated'}, status=201)
    else:
        return JsonResponse({'message': form.errors}, status=422)


# Delete Product
@csrf_exempt
def delete_product(request, id):
    del_product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        del_product.delete()
        return JsonResponse({'message': 'product deleted'}, status=201)
    else:
        return JsonResponse({'message': del_product.errors}, status=422)


# =============================Order===========================

# Show Order list
def order_list(request):
    order = {'order_list': list(Order.objects.values())}
    return JsonResponse(order, status=200, safe=False)


# Add Order
@csrf_exempt
@require_http_methods(["POST"])
def add_order(request):
    # getting api data from json_body
    order = FormOrderAdd(json_body(request))

    # validation
    if order.is_valid():
        order.save()
        return JsonResponse({'message': 'Order Added'}, status=204)
    else:
        return JsonResponse({'message': order.errors}, status=211)


# Update Order
@csrf_exempt
@require_http_methods(["PUT"])
def update_order(request, id):
    # catch the editable id (object)
    order_obj = Order.objects.get(id=id)

    # getting api data from json_body
    form = FormOrderUpdate(json_body(request), instance=order_obj)

    # validation
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Order updated'}, status=201)
    else:
        return JsonResponse({'message': form.errors}, status=422)


# Delete Order
@csrf_exempt
def delete_order(request, id):
    del_order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        del_order.delete()
        return JsonResponse({'message:': 'order delete successfully'}, status=201)
    else:
        return JsonResponse({'message': del_order.errors}, status=422)


# ==================================OrderDetails==============================

# show order details
def order_details_list(request):
    order_details = {'order_details_list': list(OrderDetails.objects.values())}
    return JsonResponse(order_details, status=200, safe=False)


# add order details
@csrf_exempt
@require_http_methods(["POST"])
def add_order_details(request):
    # getting api data from json_body
    order_details = FormOrderDetailsAdd(json_body(request))

    # validation
    if order_details.is_valid():
        order_details.save()
        return JsonResponse({'message': 'Order Added'}, status=204)
    else:
        return JsonResponse({'message': order_details.errors}, status=211)


# Update Order Details
@csrf_exempt
@require_http_methods(["PUT"])
def update_order_details(request, id):
    # catch the editable id (object)
    order_details_obj = OrderDetails.objects.get(id=id)

    # getting api data from json_body
    form = FormOrderDetailsUpdate(json_body(request), instance=order_details_obj)

    # validation
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Order Details updated'}, status=201)
    else:
        return JsonResponse({'message': form.errors}, status=422)


# Delete Order
@csrf_exempt
def delete_order_details(request, id):
    delete_order_details = get_object_or_404(Order, id=id)
    if request.method == "POST":
        delete_order_details.delete()
        return JsonResponse({'message:': 'order details delete successfully'}, status=201)
    else:
        return JsonResponse({'message': delete_order_details.errors}, status=422)

