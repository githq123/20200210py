from django.db import models
from frontuser.models import FrontUser
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

class Tag(models.Model):
    name=models.CharField(max_length=50)
    articles=models.ManyToManyField("Article",related_name="tags")

    def __str__(self):
        return "<Tag:(name:%s)>"%self.name

class Article(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ForeignKey("Category",on_delete=models.CASCADE,null=True,related_name='articles')
    author=models.ForeignKey("frontuser.FrontUser",null=True,on_delete=models.CASCADE)

    def __str__(self):
        return "<Article:(title:%s,content:%s)>"%(self.title,self.content)