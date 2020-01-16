from article.models import Article
from article.models import Author
from article.models import Reply
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'author', 'replies')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'nick_name', 'mail')

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        field = ('id', 'article', 'content', 'author')
