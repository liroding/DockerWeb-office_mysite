#-*- coding:utf-8 -*-
from django.contrib import admin
import os,sys
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,render_to_response,reverse
from django.template.context import RequestContext
#import requests
import hashlib
from InfoCollectionApp.models import PersonInfoDB,OfficeInfoDB,CustomInfoDB
from MainApp.AutoSendMail import MailHandleClass
import time
import json
#import logging
#from django.core.cache import cache
#Get an instance of a loggger
#logger = logging.getLogger('django')

#error:ascii codec can't encode characters

sys.path.append(r'/opt/mysite/myscript')
from mysqlcovert_toxls import MYSQL



PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class InfoHandleClass():
        
    def helloworld(request):
        print('[server-log]: hello world !!!')
        return HttpResponse('hello world')
    def testfunc(request):
        print('[server-log]: info html page')
        return render(request,'info.html')
    def inputinfo(request):
        print('[server-log]: input info web page')
        return render(request,'PersonalInfo/information.html')
    def infosubmit(request):
        print(request)
        print('[server-log]: info message submit')
        print(request.method)        
        name = request.POST['name']
        telephone = request.POST['telephone']
        usermessage = PersonInfoDB()
        usermessage.name = name
        usermessage.telephone = telephone
        usermessage.save()
        
        return HttpResponse('update db')

    def InfoExcel(request):

        mysql = MYSQL()

        mysql.convert('InfoCollectionApp_personinfodb', '/opt/mysite/static/downloadfile/personalinfodb.xls')
        return HttpResponse('update excel return')
    

    def office(request):
        return render(request,'Office/transationform.html')
    def purchaseorder(request):
        return render(request,'Office/purchaseorder.html')
    def purchasedetail(request):
        
        print('[server-log]: purchase datail req')
        _username = request.GET['username']
        print('username = %s' % _username)
        detaildatas = OfficeInfoDB.objects.filter(username=_username)
        '''
        dbfd = ArticlesInfoDB()
        dbfd.title = Title
        dbfd.content = Content
        dbfd.date = ArticleDate
        dbfd.author = AuthorName
        dbfd.save()
        '''
        return render(request,'Office/transationform.html',
                     {
                            'purchasedetails':detaildatas,
                     }
        ) 

    def office_query(request):
        jsonstr = request.POST['jsondata']
        _dict = json.loads(jsonstr)
        for i in range(0,len(_dict['Listdata'])):
            username = _dict['Username']
            date = _dict['Time']
            rowid = _dict['Listdata'][i]['rowid']
           
            c2 = _dict['Listdata'][i]['c2']
            c3 = _dict['Listdata'][i]['c3']
            c4 = _dict['Listdata'][i]['c4']
            c5 = _dict['Listdata'][i]['c5']
            c6 = _dict['Listdata'][i]['c6']
            _OfficeDB = OfficeInfoDB()
            _OfficeDB.username = username
            _OfficeDB.rowid = rowid
            _OfficeDB.date = date
            _OfficeDB.c2 = c2
            _OfficeDB.c3 = c3
            _OfficeDB.c4 = c4
            _OfficeDB.c5 = c5
            _OfficeDB.c6 = c6
            _OfficeDB.save()
        #    print(username)
        #    print(rowid)
        #    print(c2)
        #    print(c3)
        #    print(c4)

        return HttpResponse('update office return')
    def OfficeExcel(request):

        mysql = MYSQL()

        mysql.convert('InfoCollectionApp_officeinfodb', '/opt/mysite/static/downloadfile/officeinfodb.xls')
        return HttpResponse('update excel return')


    #### Orignal Laboratory 
    def origlab(request):
        return render(request,'OriginalLab/transationform.html')
    ###  custom collection
    def customcollection(request):
        return render(request,'CustomCollection/transationform.html')
    def uploadcontent(request):
        _dictdata = request.POST
        username = _dictdata['username']
        if username == '':
              print("kong");
              return render(request,'CustomCollection/transationform.html')
                   
        date = _dictdata['date']
        _dictlen = len(_dictdata)
        print("_dictlen=%s" % _dictlen);
        for i in range(0,int((_dictlen-1)/2)):
             _CustomDB = CustomInfoDB()
             _CustomDB.username = username
             _CustomDB.date = date
             print(i);
             titlestr = "title" + str(i)
             contentstr = "content" + str(i)
             print(titlestr)
             print(contentstr)
             for item in _dictdata:
                 if titlestr == item :
                     print("p1")
                     _CustomDB.title = _dictdata[item]
                 if contentstr == item:
                     print("p2")
                     _CustomDB.content = _dictdata[item]
                 print("dict[%s]=" % item,_dictdata[item])
             _CustomDB.save()
        #-------- send mail -----------------
        Instance = MailHandleClass("提交内容提醒","提交成功 \r\n","11","34","")
        _dictdata = Instance.GetMailAddr(username)
        mailaddr = _dictdata['mail']
        profilesetting = _dictdata['setting']
        Instance = MailHandleClass("原生态实验室[提交内容提醒]","提交成功 \r\n","11","34",mailaddr)
        if ((int(profilesetting)%10) == 1):
             Instance.AutoSendMail()
        #------------------------------------- 
        #return render(request,'CustomCollection/transationform.html')
        return HttpResponseRedirect('customcollection')
    def customcontentdetail(request):
        
        print('[server-log]: custom content  datail req')
        _username = request.GET['username']
        print('username = %s' % _username)
        detaildatas = CustomInfoDB.objects.filter(username=_username)
        return render(request,'CustomCollection/displaycontent.html',
                     {
                            'contentdetails':detaildatas,
                     }
        ) 
