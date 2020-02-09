from django.shortcuts import render,reverse,redirect
from matplotlib import font_manager

from .models import Employ,UrlModel
from .forms import SelectForm
from django.core.paginator import PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, QueryDict
from fake_useragent import UserAgent
from io import BytesIO
import base64
import numpy as np
import re
import requests
from bs4 import BeautifulSoup
# from django.db.models import Q
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")

def detail(request):
    form = SelectForm()
    # position_list = Employ.objects.all().order_by('date')
    return render(request, 'pachong/detail.html', {'form':form})
def position_spider(request):
    if request.method == 'POST':
        form = SelectForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            URL =UrlModel()
            di_value = request.POST.get('district', '')
            cp_value = request.POST.get('category_P', '')
            da_value = request.POST.get('date_time', '')
            print(di_value,da_value,cp_value)
            request.session['di_value']=di_value
            request.session['cp_value']=cp_value
            request.session['da_value']=da_value
            request.session['csrfmiddlewaretoken']=request.POST.get('csrfmiddlewaretoken','')
            url = 'https://xiaoyuan.zhaopin.com/full/0/{}_{}_0_0_{}_-1_%E5%A4%A7%E6%95%B0%E6%8D%AE_1_0'\
                .format(di_value,cp_value,da_value)
            user = UrlModel.objects.filter(url=url)
            if user:
                selsecting = SelectSpider(di_value,cp_value,da_value)
                if cp_value !='0':
                    beijing = selsecting.calculate()
                    beijing = list(beijing)
                    if cp_value=='299':
                        ass = '实习生'
                    else:
                        ass = '软件工程师'
                    po = str(ass+'岗位数')
                    name_list = ['北京', '上海', '深圳', '其他']
                    plt.xticks(range(len(beijing)), name_list, fontproperties=my_font, fontsize=15)
                    plt.bar(range(len(beijing)), beijing, color=['b', 'r', 'b', 'g'])
                    plt.title('城市职业分布图', fontproperties=my_font, fontsize=15)
                    plt.ylabel(po, fontproperties=my_font, fontsize=15)
                    plt.xlabel("城市", fontproperties=my_font, fontsize=15)
                    plt.bar(range(len(beijing)), beijing, color='rgb', tick_label=name_list)
                    save_file = BytesIO()
                    plt.savefig(save_file)
                    plot_data = save_file.getvalue()
                    imb = base64.b64encode(plot_data)
                    ims = imb.decode()
                    imd = "data:image/png;base64," + ims
                    plt.close()
                    detail = selsecting.select().order_by('date')
                    if detail:
                        page = request.GET.get('page')
                        paginator1 = Paginator(detail, 10)
                        detail = paginator1.get_page(page)
                        form2 = SelectForm()  # 'img':imd,
                        return render(request, 'pachong/detail.html',
                                      {'form': form, 'form2': form2, 'paginator': paginator1, 'img': imd,
                                       'detail': detail})
                    else:
                        return render(request, 'pachong/detail.html', {'form': form,'img':imd})
                else:
                    detail = selsecting.select().order_by('date')
                    if detail:
                        page = request.GET.get('page')
                        paginator1 = Paginator(detail, 10)
                        detail = paginator1.get_page(page)
                        form2 = SelectForm()  # 'img':imd,
                        return render(request, 'pachong/detail.html',
                                      {'form': form, 'form2': form2, 'paginator': paginator1,
                                       'detail': detail})
                    else:
                        return render(request, 'pachong/detail.html', {'form': form})
            else:# 保存数据到数据库
                URL.url = url
                URL.save()
                position_spider = PositionSpider(url,di_value,cp_value,da_value,request)
                position_spider.get_max_page()
                position_spider.parse_page()
                position_spider.save_data_to_model()
                selsecting = SelectSpider(di_value,cp_value,da_value)
                if cp_value != '0':
                    beijing = selsecting.calculate()
                    beijing = list(beijing)
                    name_list = ['北京', '上海', '深圳', '其他']
                    plt.xticks(range(len(beijing)), name_list, fontproperties=my_font, fontsize=15)
                    plt.bar(range(len(beijing)), beijing, color=['b', 'r', 'b', 'g'])
                    plt.title('职业城市分布图', fontproperties=my_font, fontsize=15)
                    plt.ylabel("职业岗位数", fontproperties=my_font, fontsize=15)
                    plt.xlabel("城市", fontproperties=my_font, fontsize=15)
                    plt.bar(range(len(beijing)), beijing, color='rgb', tick_label=name_list)
                    save_file = BytesIO()
                    plt.savefig(save_file)
                    plot_data = save_file.getvalue()
                    imb = base64.b64encode(plot_data)
                    ims = imb.decode()
                    imd = "data:image/png;base64," + ims
                    plt.close()
                    detail = selsecting.select().order_by('date')
                    if detail:
                        page = request.GET.get('page')
                        paginator1 = Paginator(detail, 10)
                        detail = paginator1.get_page(page)
                        form2 = SelectForm()  # 'img':imd,
                        return render(request, 'pachong/detail.html',
                                      {'form': form, 'form2': form2, 'paginator': paginator1, 'img': imd,
                                       'detail': detail})
                    else:
                        return render(request, 'pachong/detail.html', {'form': form,'img':imd})
                else:
                    detail = selsecting.select().order_by('date')
                    if detail:
                        page = request.GET.get('page')
                        paginator1 = Paginator(detail, 10)
                        detail = paginator1.get_page(page)
                        form2 = SelectForm()  # 'img':imd,
                        return render(request, 'pachong/detail.html',
                                      {'form': form, 'form2': form2, 'paginator': paginator1,
                                       'detail': detail})
                    else:
                        return render(request, 'pachong/detail.html', {'form': form})
        else:
            return render(request, 'pachong/detail.html', {'form': form})
    else:
        di_value=request.session.get('di_value')
        cp_value=request.session.get('cp_value')
        da_value=request.session.get('da_value')
        # form = SelectForm()
        csrf = request.session.get('csrfmiddlewaretoken')
        dic = 'csrfmiddlewaretoken='+csrf+'&district='+di_value\
              +'&category_P='+cp_value+'&date_time='+di_value
        dic = QueryDict(dic)
        form = SelectForm(dic)
        selsecting = SelectSpider(di_value, cp_value,
                                  da_value)
        # selsecting = SelectSpider(request.session.get('di_value'), request.session.get('cp_value'),
        #                           request.session.get('da_value'))
        # detail = selsecting.select().order_by('date')
        if cp_value != '0':
            beijing = selsecting.calculate()
            beijing = list(beijing)
            name_list = ['北京', '上海', '深圳', '其他']
            plt.xticks(range(len(beijing)), name_list, fontproperties=my_font, fontsize=15)
            plt.bar(range(len(beijing)), beijing, color=['b', 'r', 'b', 'g'])
            plt.title('职业城市分布图', fontproperties=my_font, fontsize=15)
            plt.ylabel("职业岗位数", fontproperties=my_font, fontsize=15)
            plt.xlabel("城市", fontproperties=my_font, fontsize=15)
            plt.bar(range(len(beijing)), beijing, color='rgb', tick_label=name_list)
            save_file = BytesIO()
            plt.savefig(save_file)
            plot_data = save_file.getvalue()
            imb = base64.b64encode(plot_data)
            ims = imb.decode()
            imd = "data:image/png;base64," + ims
            plt.close()
            detail = selsecting.select().order_by('date')
            if detail:
                page = request.GET.get('page')
                paginator1 = Paginator(detail, 10)
                detail = paginator1.get_page(page)
                form2 = SelectForm()  # 'img':imd,
                return render(request, 'pachong/detail.html',
                              {'form': form, 'form2': form2, 'paginator': paginator1, 'img': imd,
                               'detail': detail})
            else:
                return render(request, 'pachong/detail.html', {'form': form})
        else:
            detail = selsecting.select().order_by('date')
            if detail:
                page = request.GET.get('page')
                paginator1 = Paginator(detail, 10)
                detail = paginator1.get_page(page)
                form2 = SelectForm()  # 'img':imd,
                return render(request, 'pachong/detail.html',
                              {'form': form, 'form2': form2, 'paginator': paginator1,
                               'detail': detail})
            else:
                return render(request, 'pachong/detail.html', {'form': form})



class PositionSpider(object):
    def __init__(self,url,di_value,cp_value,da_value,request):
        # self.ua = UserAgent(),di_value,cp_value,ch_value,pro_value,da_value,o_value
        self.headers = {'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:67.0)Gecko/20100101Firefox/67.0'}
        self.data = list()
        self.url = url
        self.di_value = di_value
        self.cp_value = cp_value
        # self.ch_value = ch_value
        # self.pro_value = pro_value
        self.da_value = da_value
        self.request = request
        # self.o_value = o_value


    def get_max_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            # print(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)
            a = soup.find_all("span",class_="pageItem")
            # a = soup.select('span[class="pageItem"]')
            # print(a)
            if a != []:
                # print(self.url)
                max_page = eval(a[-1].text)
                # 使用eval是字符串转化为字典格式
                return max_page
            else:
                print("请求失败1 status:{}".format(response.status_code))
                return 0
        else:
            print("请求失败2 status:{}".format(response.status_code))
            return 0

    def parse_page(self):
        max_page = self.get_max_page()
        for i in range(1, max_page + 1):
            url = self.url[:-4]
            url = '{}_{}_0'.format(url,i)

            response = requests.get(url)
            soup = BeautifulSoup(response.content,'lxml',from_encoding='utf-8')
            ul = soup.find_all('ul', class_='searchResultListUl')
            li_list = ul[0].select("li")
            # print(li_list)
            for li in li_list:
                detail = dict()
                # print(li)
                detail['position'] = li.select('a[target="_blank"]')[0].get_text()
                detail['company'] = li.select('p[class="searchResultCompanyname"]')[0].get_text()
                # detail['company'] = position_info[0]
                # detail['salary'] = li.select('div[class= "position_require')[0].get_text()
                # detail['date'] = position_info[2] # 从字符串任意位置匹配
                detail['location'] = li.select('em[class="searchResultJobCityval"]')[0].get_text()
                d = li.select('p[class="pt15 pb10"]')[0].select('span')[0].get_text()
                detail['date'] = d[7:-1]
                detail['di_value'] = self.di_value
                detail['cp_value'] = self.cp_value
                # detail['ch_value']=self.ch_value
                # detail['pro_value']=self.pro_value
                detail['da_value'] = self.da_value
                # detail['o_value']=self.o_value
                self.data.append(detail)

    def save_data_to_model(self):
        for item in self.data:
            new_item = Employ()
            new_item.position = item['position']
            new_item.company = item['company']
            # new_item.salary = item['salary']
            new_item.location = item['location']
            new_item.date = item['date']
            new_item.di_value = item['di_value']
            new_item.cp_value = item['cp_value']
            # new_item.ch_value = item['ch_value']
            # new_item.pro_value = item['pro_value']
            new_item.da_value = item['da_value']
            # new_item.origin = item['o_value']
            # new_item.date = item['date']
            new_item.save()
class SelectSpider(object):
    def __init__(self,di_value,cp_value,da_value):
        self.di_value = di_value
        self.cp_value = cp_value
        # self.ch_value = ch_value
        # self.pro_value = pro_value
        self.da_value = da_value
        # self.o_value = o_value
    def select(self):
        # print(self.da_value)
        pcdl = Employ.objects.filter(da_value=self.da_value,di_value=self.di_value,cp_value=self.cp_value)
        return pcdl
    def calculate(self):
        beijing = Employ.objects.filter(cp_value=self.cp_value,di_value='530')
        beijing = len(beijing)
        shanghai = Employ.objects.filter(cp_value=self.cp_value,di_value='538')
        shanghai = len(shanghai)
        shenzhen = Employ.objects.filter(cp_value=self.cp_value,di_value='765')
        shenzhen = len(shenzhen)
        others = Employ.objects.filter(cp_value=self.cp_value,di_value='0')
        others = len(others)
        return beijing,shanghai,shenzhen,others
        # if user:
        #     for i in user:
        #         p = i.position
        #         c = i.company
        #         d = i.date
        #         l = i.location
        #         print(p, c, d, l)
        # else:
        #     print("null")