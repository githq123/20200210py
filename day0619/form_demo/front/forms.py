from django import forms
from django.core import validators
from .models import User

class BaseForm(forms.Form):
    def get_errors(self):
        errors=self.errors.get_json_data()
        new_errors={}
        for key,message_dicts in  errors.items():
            messages=[]
            # print(message_dicts)
            for message_dict in message_dicts:
                message=message_dict['message']
                messages.append(message)
            new_errors[key]=messages
        return new_errors


class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=6, label="标题", error_messages={"min_length": "最少不能少于6个字符"})
    content = forms.CharField(widget=forms.Textarea, label="内容", error_messages={"required": "必须要写content这个字段"})
    email = forms.EmailField(label="邮箱", error_messages={"required": "必须要传email字段"})
    reply = forms.BooleanField(required=False, label="是否回复")

# class RegisterForm(forms.Form):
class RegisterForm(BaseForm):
    username=forms.CharField(max_length=100)
    telephone=forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}',message="请输入正确格式手机号")])
    email=forms.CharField(validators=[validators.EmailValidator(message="请输入正确格式邮箱")])
    pwd1=forms.CharField(max_length=20,min_length=6)
    pwd2=forms.CharField(max_length=20,min_length=6)

    def clean_telephone(self):
        telephone=self.cleaned_data.get('telephone')
        exists=User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message="%s:已经注册"%telephone)#抛出错误
        return telephone


    #如果走到这里 说明所有字段验证成功
    def clean(self):
        cleaned_data=super(RegisterForm,self).clean()
        pwd1=cleaned_data.get('pwd1')
        pwd2=cleaned_data.get('pwd2')
        if pwd1!=pwd2:
            raise forms.ValidationError(message="密码不一致") # 抛出错
        return cleaned_data
