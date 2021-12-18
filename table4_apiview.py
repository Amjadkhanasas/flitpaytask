from flit.models import Table4_tradetype
from flit.serializers import table4serializer
from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




class Table4_tradetypeModelViewSet(viewsets.ModelViewSet):
    queryset =Table4_tradetype.objects.all()
    serializer_class = table4serializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated]