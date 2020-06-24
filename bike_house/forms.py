from django import forms
from bike_house.models import Place, BikeHouse

class FormPlaceAdd(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"


class FormBikeAdd(forms.ModelForm):
    class Meta:
        model = BikeHouse
        fields = "__all__"