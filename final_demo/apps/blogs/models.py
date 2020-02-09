from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    text = models.TextField('内容')
    total_views = models.PositiveIntegerField(default=0)
    tags = TaggableManager(blank=True)
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='articles')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title