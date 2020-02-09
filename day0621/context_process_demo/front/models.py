from django.db import models
from django.core import validators
# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=100,validators=[validators.MinLengthValidator(6)])
    password=models.CharField(max_length=30,validators=[validators.MinLengthValidator(6)])
    telephone = models.CharField(max_length=11, validators=[validators.RegexValidator(r'1[34578]\d{9}',message='请输入正确格式的手机号码！')])
