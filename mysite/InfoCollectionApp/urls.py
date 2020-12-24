from django.urls import path
from InfoCollectionApp.InfoAppHandle import InfoHandleClass
urlpatterns =[

      path('helloworld',InfoHandleClass.helloworld),
      ################## [testfunc] ####################
      path('inputinformation',InfoHandleClass.inputinfo),
      path('infosubmit',InfoHandleClass.infosubmit),
      path('infoexcel',InfoHandleClass.InfoExcel),

      ## office
      path('office',InfoHandleClass.office),
      path('purchaseorder',InfoHandleClass.purchaseorder),
      path('purchasedetail',InfoHandleClass.purchasedetail),
      path('office_query',InfoHandleClass.office_query),
      path('officeexcel',InfoHandleClass.OfficeExcel),

      ## original laboratory
      path('origlab',InfoHandleClass.origlab),
      ## custom collection
      path('customcollection',InfoHandleClass.customcollection),
      path('customcontentdetail',InfoHandleClass.customcontentdetail),
      path('uploadcontent',InfoHandleClass.uploadcontent),
]
 
