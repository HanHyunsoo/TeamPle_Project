from django.db import models
from team.models import Team
from account.models import User


# Create your models here.
def article_file_path(instance, filename):
    return 'articles/{}/files/{}'.format(instance.article.pk, filename)


def article_image_path(instance, filename):
    return 'articles/{}/images/{}'.format(instance.article.pk, filename)


def comment_file_path(instance, filename):
    return 'articles/{}/comment/{}/files/{}'.format(instance.comment.article.pk, instance.comment.pk, filename)


def comment_image_path(instance, filename):
    return 'articles/{}/comment/{}/images/{}'.format(instance.comment.article.pk, instance.comment.pk, filename)


class Article(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='articles')
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=30)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ArticleFile(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='files')
    file_url = models.FileField(upload_to=article_file_path)


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image_url = models.FileField(upload_to=article_image_path)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class CommentFile(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    file_url = models.FileField(upload_to=comment_file_path)


class CommentImage(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    image_url = models.FileField(upload_to=comment_image_path)
