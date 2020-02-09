#coding=utf-8
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import jieba
excludes={"一个","两人","我们","贾府","如今","说道","知道","什么","那里","你们","这里","出来","他们","姑娘","起来","众人","自己","一面","只见","怎么","奶奶"
            ,"两个","没有","不是","不知","这个","听见","这样","进来","咱们","就是","告诉","东西","回来","只是","大家","老爷","只得","这些","那些","不敢","丫头"
            ,"出去","所以"}
txt = open("红楼梦.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "贾母" or word == "老太太":
        rword = "贾母"
    elif word == "凤姐" or word == "王夫人":
        rword = "王熙凤"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
ss=items[:10]
dictdata = {}
for l in ss:
    dictdata[l[0]] = l[1]
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
graph = np.array(Image.open("1129.jpg"))
wc = WordCloud(background_color="white",font_path='./fonts/simhei.ttf',max_words=50,mask=graph,margin=2)
wc.generate_from_frequencies(dictdata)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
wc.to_file('dream.png')
