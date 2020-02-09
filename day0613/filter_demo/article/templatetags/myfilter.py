from django import template
from datetime import datetime
register=template.Library()

@register.filter#将过滤器注册到系统中
def time_since(value):
    # 小于一分钟显示刚刚
    # 小于一小时显示几分钟之前
    # 小于24小时显示几小时之前
    # 小于30天显示几天前
    # 其他时间显示年月日
    if not isinstance(value,datetime):
        return value
    now=datetime.now()
    timestamp=(now-value).total_seconds()
    if timestamp<60:
        return "刚刚"
    elif timestamp>60 and timestamp<60*60:
        minutes=int(timestamp/60)
        return "%s 分钟以前"%minutes
    elif timestamp>60*60 and timestamp<60*60*24:
        hours=int(timestamp/60)
        return "%s 分钟以前"%hours
    elif timestamp>60*60*24 and timestamp<60*60*24*30:
        days=int(timestamp/60)
        return "%s 分钟以前"%days
    else:
        return value.strftime("%Y/%m/%d %H:%M")