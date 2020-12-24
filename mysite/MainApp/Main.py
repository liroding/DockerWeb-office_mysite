#-*- coding:utf-8 -*-
from django.contrib import admin
import os,sys
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,render_to_response,redirect
from django.template.context import RequestContext
#import requests
import hashlib
from MainApp.models import ArticlesInfoDB
from InfoCollectionApp.models import PersonInfoDB,OfficeInfoDB,CustomInfoDB
from LoginApp.models import LoginDB  
import time
import os
#import logging
#from django.core.cache import cache
#Get an instance of a loggger
#logger = logging.getLogger('django')

#error:ascii codec can't encode characters


sys.path.append(r'/opt/mysite/myscript')
from mysqlcovert_toxls import MYSQL




PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SERVERIP = "39.107.48.2:8080"

class MainHandleClass():
        
    def helloworld(request):
        print('[server-log]: hello world !!!')
        return HttpResponse('hello world')
    
    def indexpage(request):
        print('[server-log]: request index page')
        return render(request,'index.html')
    '''
    def articlepage(request):
        print('[server-log]: request article page')
        return render(request,'article.html')
    '''
    def addnewarticles(request):
        
        redirecturl = '/main/article?type=previous&num=0'
        print('[server-log]: add new articles submit')
        
        Title = request.POST['title']
        Content = request.POST['content']
        
        AuthorName = request.POST['AuthorName']
        ArticleDate = request.POST['ArticleDate']
        
        dbfd = ArticlesInfoDB()
        dbfd.title = Title
        dbfd.content = Content
        dbfd.date = ArticleDate
        dbfd.author = AuthorName
        dbfd.save()
        
        return HttpResponseRedirect(redirecturl)

    def articlepage(request):
        print('[server-log]: display articles rq')
        _type = request.GET['type']
        _num =  request.GET['num']
 #       if _num != 0:
 #              if _type == 'next':
        totlenum = ArticlesInfoDB.objects.count()
        reqtailnum = int(_num) + 5
        if reqtailnum >= totlenum: 
            reqtailnum = totlenum;
        allarticles = ArticlesInfoDB.objects.all()[int(_num):reqtailnum]
        return render(request,'article.html',
                     {
                            'articles':allarticles,
                            'totlenumlist':range(0, totlenum)
                     }
        ) 
                   
                   #Title = request.POST['title']
                   #Content = request.POST['content']
         
#        return HttpResponse('display articles return')



    def displayarticles(request):
        print('[server-log]: display articles rq')
        _id = request.GET['id']
        print("id=%s" % _id)
        allarticles = ArticlesInfoDB.objects.all()
        article = None
        for a in allarticles:
            if a.id == int(_id):
                 article = a
                 break
        return render(request,'showarticle.html',
               {
                  'article':article
               })
        #allarticles = ArticlesInfoDB.objects.all()
        #return HttpResponse('display articles return')
                   
    def updatearticle(request):

        print('[server-log]: update articles rq')
        _articleid = request.POST['articleid']
        newcontent = request.POST['newcontent']
        print("_articleid=%s" % _articleid)
        print("_article content=%s" % newcontent)


        allarticles = ArticlesInfoDB.objects.all()
        article = None
        for a in allarticles:
            if a.id == int(_articleid):
                 a.content = newcontent
                 a.save()
                 break
        return HttpResponse('update articles return')

    def deletearticle(request):
        redirecturl = '/main/article?type=previous&num=0'
        print('[server-log]: delete articles rq')
        _articleid = request.GET['id']
        print("_articleid=%s" % _articleid)

        ArticlesInfoDB.objects.filter(id=_articleid).delete()
       
        return HttpResponseRedirect(redirecturl)

    def download(request):
        print('[server-log]: request download page')
        return render(request,'download.html')

    def informationservice(request):
        print('[server-log]: request information service page')
        return render(request,'informationservice.html')

    ######## profile setting ############# begin
    def profilesetting(request):
        print('[server-log]: request profile setting page')
        return render(request,'profilesetting.html')
    def currentsetting(request):
        print('[server-log]: request current setting page')
        _username = request.GET['username']
        detaildatas  = LoginDB.objects.all()
        for a in detaildatas:
            if a.user == _username:
                 return HttpResponse(a.profilesetting)

    def updateprofilesetting(request):
        print('[server-log]: request update profile setting page')
        _username = request.GET['username']
        _settingvalue = request.POST['value']
        _settingtype  = request.POST['type']
        detaildatas   = LoginDB.objects.all()
        print(_settingtype)
        print(_settingvalue)
        for a in detaildatas:
            if a.user == _username:
                 if _settingtype == 'isopenmail':
                    print("p1")
                    _tmpvalue = a.profilesetting
                    _tmplist = list(_tmpvalue)
                    _tmplist[0] = _settingvalue
                    print("p2")
                    _tmpvalue = ''.join(_tmplist)
                    a.profilesetting = _tmpvalue
                    print("p3")
                    a.save()
                 return HttpResponse('update profile setting return')
        print('[server-log]: value='+ _settingvalue)
    #+++++++++++++++  end  ++++++++++++++++




    def ArticleContentExcel(request):
       
        mysql = MYSQL()
        
        #mysql.convert('InfoCollectionApp_personinfodb', '/opt/mysite/static/downloadfile/mysqldb.xls')
        mysql.convert('MainApp_articlesinfodb', '/opt/mysite/static/downloadfile/articlecontentdb.xls')
        return HttpResponse('update excel return')
