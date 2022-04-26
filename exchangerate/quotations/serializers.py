from rest_framework import serializers
from .models import UsdQuotation

class UsdQuotationSerializer(serializers.ModelSerializer):
  class Meta:
    model = UsdQuotation
    fields = [
      'id',
      'date',
      'euro_rate',
      'real_rate',
      'yen_rate'
    ]