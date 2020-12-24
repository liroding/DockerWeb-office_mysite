from django.urls import path
from MainApp.Main import MainHandleClass

from InfoCollectionApp.InfoAppHandle import InfoHandleClass


urlpatterns =[

      ################## [testfunc] ####################
      path('helloworld',MainHandleClass.helloworld),
      
      path('index',MainHandleClass.indexpage),
      path('article',MainHandleClass.articlepage),
      path('addnewarticles',MainHandleClass.addnewarticles),
      path('displayarticles',MainHandleClass.displayarticles),
      path('updatearticle',MainHandleClass.updatearticle),
      path('deletearticle',MainHandleClass.deletearticle),
      path('setting',MainHandleClass.profilesetting),
      path('currentsetting',MainHandleClass.currentsetting),
      path('updateprofilesetting',MainHandleClass.updateprofilesetting),


      path('informationservice',MainHandleClass.informationservice),
      path('inputinformation',InfoHandleClass.inputinfo),
      #download 
      path('download',MainHandleClass.download),
      path('articlecontentexcel',MainHandleClass.ArticleContentExcel), #download article content excel

]
 
