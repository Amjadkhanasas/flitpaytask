
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from flit.apiview import table1_apiview
from flit.apiview import table2_apiview
from flit.apiview import table3_apiview
from flit.apiview import table4_apiview
from flit.apiview import table5_apiview
from flit.apiview import table6_apiview
from flit.apiview import login_apiview

from rest_framework.generics import CreateAPIView

router = DefaultRouter()

   
router.register('create_temp_user', table1_apiview.Table1_TempuserModelViewSet,basename='Table1_TempuserModelViewSet'),
router.register('add_new_customer', table2_apiview.Table2_CustomerModelViewSet,basename='Table2_CustomerModelViewSet'),
router.register('add_new_tradesman', table3_apiview.Table3_tradesmanModelViewSet,basename='Table3_tradesmanModelViewSet'),
router.register('check_trade', table4_apiview.Table4_tradetypeModelViewSet,basename='Table4_tradetypeModelViewSet'),
router.register('book_tradesman', table5_apiview.Table5_booktradesmanModelViewSet,basename='Table5_booktradesmanModelViewSet'),
router.register('img_upload', table6_apiview.Table6_Image_UplodadModelViewSet,basename='Table6_Image_UplodadModelViewSet'),





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh_view'),
    path('login/',login_apiview.CreateAPIView.as_view(),name='Create_API_View'),
    
]
    