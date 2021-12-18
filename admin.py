from django.contrib import admin

from .models import *

class Table1_TempuserAdmin(admin.ModelAdmin):
    list_display= ('mobilenumber',)
admin.site.register(Table1_Tempuser, Table1_TempuserAdmin)

class Table2_CustomerAdmin(admin.ModelAdmin):
    list_display= ('mobileNumber','customername','dob','email','status','created_date')
admin.site.register(Table2_Customer, Table1_TempuserAdmin)

class Table4_tradetypeAdmin(admin.ModelAdmin):
    list_display= ('tradeid','tradetype','status')
admin.site.register(Table4_tradetype,Table4_tradetypeAdmin)


class Table3_tradesmanAdmin(admin.ModelAdmin):
    list_display= ('tradesman_name','Table_4_id','status','created_date')
admin.site.register(Table3_tradesman,Table3_tradesmanAdmin)


class Table6_Image_UplodadAdmin(admin.ModelAdmin):
    list_display= ('status','Table2_id','imagepath','created_date')
admin.site.register(Table6_Image_Uplodad,Table6_Image_UplodadAdmin)


class Table5_booktradesmanAdmin(admin.ModelAdmin):
    list_display= ('Table2_id','Table3_id','time','time','status',)
admin.site.register(Table5_booktradesman,Table5_booktradesmanAdmin)

