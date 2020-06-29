from django.contrib import admin
from .models import *
# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']


class BikeHouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cc', 'model', 'price', 'place']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'bike_house']


admin.site.register(Place, PlaceAdmin)
admin.site.register(BikeHouse, BikeHouseAdmin)
admin.site.register(Customer, CustomerAdmin)
