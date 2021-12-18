from flit.models import Table3_tradesman
from flit.serializers import table3serializer
from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Table3_tradesmanModelViewSet(viewsets.ModelViewSet):
    queryset = Table3_tradesman.objects.all()
    serializer_class = table3serializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated]