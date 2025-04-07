from rest_framework import serializers
from .models import CustomerDetails

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = '__all__'
