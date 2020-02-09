from django.db import models

# Create your models here.
class UrlModel(models.Model):
    url = models.CharField(max_length=256)

class Employ(models.Model):
    position = models.CharField(max_length=50,verbose_name='职位')
    company = models.CharField(max_length=100,verbose_name='公司')
    date = models.CharField(max_length=100,verbose_name='发布时间')
    location = models.CharField(max_length=20,verbose_name='地点')
    da_value = models.CharField(max_length=100,verbose_name='时间返回值')
    di_value = models.CharField(max_length=100,verbose_name='地点类型返回值')
    cp_value = models.CharField(max_length=100,verbose_name='职位类型返回值')