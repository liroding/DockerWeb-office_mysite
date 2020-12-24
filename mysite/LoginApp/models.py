from django.db import models

# Create your models here.

class LoginDB(models.Model):
    user = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    mail = models.CharField(max_length = 30 ,default="")
    profilesetting = models.CharField(max_length = 8 ,default="0")

    def __str__(self):
        return 'name:'+self.user+','+self.password

