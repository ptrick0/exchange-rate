from django import forms
from .models import UsdQuotation

class UsdQuotationForm(forms.ModelForm):
    class Meta():
        model = UsdQuotation
        fields = '__all__'
