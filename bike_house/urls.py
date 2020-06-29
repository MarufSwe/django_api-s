from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('place/', views.place_list),
    path('create_place/', views.add_place),
    # path('edit_place/<int:id>', UpdatePlace.as_view()),
    path('edit_place/<int:id>', views.update_place),
    path('delete_place/<int:id>/', views.delete_place),

    path('create_bike/', views.add_bike),
    path('bike_list/', views.bike_list),
    path('delete_bike/<int:id>/', views.delete_bike),

    path('customer_list/', views.customer_list),
    path('create_customer/', views.add_customer),

]