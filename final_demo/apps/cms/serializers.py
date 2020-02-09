from rest_framework import serializers
from apps.blogs.models import Article

class  ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'text']