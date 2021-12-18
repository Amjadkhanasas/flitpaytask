from django.db.models import fields
from flit.models import Table3_tradesman

from rest_framework import serializers


class Table3_tradesmanSerializer(serializers.ModelSerializer):

	class Meta:
		model = Table3_tradesman
		fields = '__all__'