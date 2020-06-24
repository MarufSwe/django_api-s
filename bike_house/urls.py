from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('place/', views.place_list),
    path('create_place/', views.add_place),

    path('create_bike/', views.add_bike)
]