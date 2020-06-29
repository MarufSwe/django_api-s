from django import forms
from bike_house.models import Place, BikeHouse, Customer


class FormPlaceAdd(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"


class FormPlaceEdit(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"


class FormBikeAdd(forms.ModelForm):
    class Meta:
        model = BikeHouse
        fields = "__all__"


class FormCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
