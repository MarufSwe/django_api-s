from django.urls import path
from . import views
from .views import UpdateCategory

urlpatterns = [
    path('category/', views.category_list),
    path('add_category/', views.add_category),
    path('update_category/<int:id>/', UpdateCategory.as_view()),
    path('del_category/<int:id>/', views.delete_category),

    path('product/', views.product_list),
    path('add_product/', views.add_product),
    path('update_product/<int:id>/', views.update_product),
    path('del_product/<int:id>/', views.delete_product),

]