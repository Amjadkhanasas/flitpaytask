from flit.models import Table2_Customer
from flit.serializers import table2serializer
from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Table2_CustomerModelViewSet(viewsets.ModelViewSet):
      queryset = Table2_Customer.objects.all()
      serializer_class = table2serializer
      authentication_classes= [TokenAuthentication]
      permission_classes = [IsAuthenticated]
