from rest_framework import serializers
from .models import Customer 

class CustomerSerializer(serializers.ModelSerializer):

    # the Meta class will specify the model and fields to serialize
    class Meta:
        model = Customer
        fields = ('pk','first_name', 'last_name', 'email', 'phone','address','description')

