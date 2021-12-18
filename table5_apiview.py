from flit.models import Table5_booktradesman
from flit.serializers import table5serializer
from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class Table5_booktradesmanModelViewSet(viewsets.ModelViewSet):
    queryset = Table5_booktradesman.objects.all()
    serializer_class = table5serializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated]

   
    