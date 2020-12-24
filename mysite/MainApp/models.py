from django.db import models

# Create your models here.

class ArticlesInfoDB(models.Model):
	title = models.CharField(max_length = 100,default = '')	
	content = models.CharField(max_length = 10000,default = '')
	date = models.CharField(max_length = 20,default = '')	
	author = models.CharField(max_length = 20,default = '')	
       	
