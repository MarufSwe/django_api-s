from django import forms
from products_category.models import *


class FromCategoryAdd(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class FromCategoryUpdate(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class FromProductAdd(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class FromProductUpdate(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
