from flit.models import Table1_Tempuser
from flit.serializers import table1serializer
from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Table1_TempuserModelViewSet(viewsets.ModelViewSet):
    queryset = Table1_Tempuser.objects.all()
    serializer_class = table1serializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated]