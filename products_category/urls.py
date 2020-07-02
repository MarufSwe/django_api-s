from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category_list),
    path('add_category/', views.add_category),
    path('update_category/<int:id>/', views.update_category),
    path('del_category/<int:id>/', views.delete_category),

    path('product/', views.product_list),
    path('add_product/', views.add_product),
    path('update_product/<int:id>/', views.update_product),
    path('del_product/<int:id>/', views.delete_product),

    path('order/', views.order_list),
    path('add_order/', views.add_order),
    path('update_order/<int:id>/', views.update_order),
    path('del_order/<int:id>/', views.delete_order),

    path('order_details/', views.order_details_list),
    path('add_order_details/', views.add_order_details),
    path('update_order_details/<int:id>/', views.update_order_details),
    path('delete_order_details/<int:id>/', views.delete_order_details),

]