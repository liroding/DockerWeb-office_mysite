from django.contrib import admin
from . models import PersonInfoDB,OfficeInfoDB,CustomInfoDB
# Register your models here.

admin.site.register(PersonInfoDB)
admin.site.register(OfficeInfoDB)
admin.site.register(CustomInfoDB)
