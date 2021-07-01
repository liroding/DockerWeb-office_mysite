from django.db import models

# Create your models here.

class PersonInfoDB(models.Model):
        name = models.CharField(max_length = 20,default = '')
        telephone = models.CharField(max_length = 20,default = '')
        mailaddr = models.CharField(max_length = 30,default = '')
        password = models.CharField(max_length = 20,default = '')
class OfficeInfoDB(models.Model):
        username = models.CharField(max_length = 20,default = '')
        rowid = models.CharField(max_length = 10,default = '')
        date = models.CharField(max_length = 20,default = '')
        c2 = models.CharField(max_length = 20,default = '')
        c3 = models.CharField(max_length = 50,default = '')
        c4 = models.CharField(max_length = 50,default = '')
        c5 = models.CharField(max_length = 20,default = '')
        c6 = models.CharField(max_length = 50,default = '')
class CustomInfoDB(models.Model):
        username = models.CharField(max_length = 20,default = '')
        title = models.CharField(max_length = 50,default = '')
        content = models.CharField(max_length = 1000,default = '')
        date = models.CharField(max_length = 20,default = '')
