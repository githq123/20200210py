from django import forms

DISTRICT_CHOICES =(('0','其他'),
                   ('530','北京'),
                   ('538','上海'),
                   ('765','深圳'))
CATEGORY_P_CHOICES =(('0','不限'),
                     ('299','实习生'),
                     ('45','软件工程师'),
                     )
DATE_CHOICES =(('0','不限'),
                ('1','一天内'),
               ('2','三天内'),
               )
class SelectForm(forms.Form):
    district = forms.CharField(label="地区范围",widget=forms.widgets.Select(choices=DISTRICT_CHOICES))
    category_P = forms.CharField(label="职位类型",widget=forms.widgets.Select(choices=CATEGORY_P_CHOICES))
    date_time= forms.CharField(label="发布时间",widget=forms.widgets.Select(choices=DATE_CHOICES))
