from django import forms
from apps.forms import FormMiXin
from django.core import validators
from .models import User
from django.core.cache import cache

class LoginForm(forms.Form,FormMiXin):
    telephone=forms.CharField(max_length=11,validators=[validators.RegexValidator('r1[345678]\d{9}',message='请输入正确格式的手机号')])
    password=forms.CharField(max_length=30,min_length=6,error_messages={"max_length":"密码最多不超过30位","min_length":"密码最少不低于六位"})
    remember=forms.IntegerField(required=False)
class RegisterForm(forms.Form,FormMiXin):
    telephone = forms.CharField(max_length=11,validators=[validators.RegexValidator('r1[345678]\d{9}', message='请输入正确格式的手机号')])
    username=forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=30, min_length=6,error_messages={"max_length": "密码最多不超过30位", "min_length": "密码最少不低于六位"})
    password2= forms.CharField(max_length=30, min_length=6,error_messages={"max_length": "密码最多不超过30位", "min_length": "密码最少不低于六位"})
    img_captcha=forms.CharField(min_length=4,max_length=6)
    sms_captcha=forms.CharField(min_length=4,max_length=6)

    def clean(self):
        cleaned_data=super(RegisterForm,self).clean()
        password1=cleaned_data.get("password1")
        password2=cleaned_data.get("password2")
        if password2!=password1:
            raise forms.ValidationError("两次密码输入不一致")

        # text=cleaned_data.get('captcha')
        # cache.get(text.lower())
        
        return cleaned_data

