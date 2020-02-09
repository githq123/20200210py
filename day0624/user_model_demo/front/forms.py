from django import forms
from django.contrib.auth import get_user_model
#get_user_model导入用户模型
class LoginForm(forms.ModelForm):
    remember=forms.IntegerField(required=False)
    telephone=forms.CharField(max_length=11)
    class Meta:
        model=get_user_model()
        fields=['password']
