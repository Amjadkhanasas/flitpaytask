from django.db.models import fields
from flit.models import Table6_Image_Uplodad

from rest_framework import serializers


class Table6_Image_UplodadSerializer(serializers.ModelSerializer):

	class Meta:
		model = Table6_Image_Uplodad
		fields = '__all__'