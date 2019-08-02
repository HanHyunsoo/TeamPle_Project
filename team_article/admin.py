from django.contrib import admin
from .models import Article, ArticleFile, ArticleImage, Comment, CommentFile, CommentImage
# Register your models here.
admin.site.register(Article)