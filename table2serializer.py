from flit.models import Table2_Customer
from rest_framework import serializers


class Table2_CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table2_Customer
        fields = '__all__'


class Table2_updateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table2_Customer
        fields = '__all__'
    def __init__(self, *args, **kwargs):
         kwargs['partial'] = True
         super(Table2_CustomerSerializer, self).__init__(*args, **kwargs)
         