from flit.models import Table6_Image_Uplodad
from flit.serializers import table6serializer
from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Table6_Image_UplodadModelViewSet(viewsets.ModelViewSet):
    queryset = Table6_Image_Uplodad.objects.all()
    serializer_class = table6serializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated]
