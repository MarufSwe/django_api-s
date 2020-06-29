from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import *
from .helper import json_body
from .models import *


# Create your views here.

# Show category list
def category_list(request):
    category = {'category_list': list(Category.objects.values())}
    return JsonResponse(category, status=200, safe=False)


# Add Category
@csrf_exempt
@require_http_methods(["POST"])
def add_category(request):
    # getting api data
    category = FromCategoryAdd(json_body(request))

    # validation
    if category.is_valid():
        category.save()
        return JsonResponse({'message': 'product added'}, status=201, safe=False)
    else:
        return JsonResponse({'message': category.errors}, status=422)


# Update Category
@method_decorator(csrf_exempt, name='dispatch')
class UpdateCategory(View):
    def put(self, request, id=None):

        # catch the editable id (object)
        category_obj = Category.objects.get(id=id)

        # getting api data
        form = FromCategoryUpdate(json_body(request), instance=category_obj)

        # validation
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Category Updated!"}, status=201, safe=False)
        else:
            return JsonResponse({"message": form.errors}, status=422, safe=False)


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
    product = FromProductAdd(json_body(request))

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
    form = FromProductUpdate(json_body(request), instance=product_obj)

    # validation
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'product updated'}, status=201)
    else:
        return JsonResponse({'message': form.errors}, status=422)


# Delete Product
@csrf_exempt
def delete_product(request, id):
    del_product = get_object_or_404(Product,id=id)
    if request.method == "POST":
        del_product.delete()
        return JsonResponse({'message': 'product deleted'}, status=201)
    else:
        return JsonResponse({'message': del_product.errors}, status=422)