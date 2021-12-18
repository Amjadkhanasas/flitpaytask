from django.db.models import fields
from flit.models import Table1_Tempuser

from rest_framework import serializers


class Table1_TempuserSerializer(serializers.ModelSerializer):

	class Meta:
            model = Table1_Tempuser
            fields = '__all__'