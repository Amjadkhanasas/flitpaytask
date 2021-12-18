from django.db.models import fields
from flit.models import Table5_booktradesman

from rest_framework import serializers


class Table5_booktradesmanSerializer(serializers.ModelSerializer):

	class Meta:
		model = Table5_booktradesman
		fields = '__all__'