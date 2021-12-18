from django.contrib.auth.models import User
from rest_framework import response
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate,login
from rest_framework import status
from rest_framework.response import Response
from flit.models import *
from flit.serializers.table1serializer import Table1_TempuserSerializer
from flit.serializers.table2serializer import Table2_CustomerSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated





class generate_otp(CreateAPIView):
    queryset = Table1_Tempuser.objects.all
    Serializer_class= Table1_TempuserSerializer
    def post(self, request, format=None):
        ser = self.Table1_TempuserSerializer(
            data = request.data,
                )
        if ser.is_valid():
            ser.save()
            return Response({'msg':' verification otp sent on the mobile number'})  
            
class TokenObtainPairView(CreateAPIView):
    queryset = Table2_Customer.objects.all
    Serializer_class= Table2_CustomerSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        ser = self.Table2_CustomerSerializer(
            data = request.data,context={'request':request}
        )
        if ser.is_valid():
            pk=request.data.get("pk")
            otp=request.data.get("otp")
                          
            user=authenticate(request, pk=pk,otp=otp)
            return response(response,status=status.HTTP_200_OK)
            
        if ObjectDoesNotExist:
            return response('customer doesnot exist')
            

        

        



