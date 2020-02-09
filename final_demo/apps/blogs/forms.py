from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):  # 继承ModelForm类
    class Meta:
        model = Article  # 具体要操作那个模型
        fields = ['title', 'text','tags']  # 允许编辑的字段
