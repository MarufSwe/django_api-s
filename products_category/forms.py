from django import forms
from products_category.models import *


class FormCategoryAdd(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class FormCategoryUpdate(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class FormProductAdd(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class FormProductUpdate(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class FormOrderAdd(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class FormOrderUpdate(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class FormOrderDetailsAdd(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = "__all__"


class FormOrderDetailsUpdate(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = "__all__"