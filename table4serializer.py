from django.db.models import fields
from flit.models import Table4_tradetype

from rest_framework import serializers


class Table4_tradetypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Table4_tradetype
		fields = '__all__'