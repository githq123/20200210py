from django import forms
from .models import Book, User


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = "__all__"  # 应用模型中所有字段
        # fields = ['title','page']#应用模型中指定的字段
        # exclude = ['price']#除了这个字段模型字段全用
        error_messages = {
            'page': {
                'required': '请传入page参数',
                'invalid': '请传入一可用的page参数'
            },
            'title': {
                'max_length': '最大长度不能超过100字符'
            },
            'price': {
                'max_value': '最大值不能超过1000元'
            }
        }


class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pwd1 = self.cleaned_data.get('pwd1')
        pwd2 = self.cleaned_data.get('pwd2')
        if pwd2 != pwd1:
            raise forms.ValidationError(message="两次密码输入不一致")
        return cleaned_data

    class Meta:
        model = User
        exclude = ['password']
