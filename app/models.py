import re
from django.db import models
from django.contrib.auth.models import AbstractUser 

ARTICLE_STATUS = (
            ('draft', 'Draft'),
            ('inprogress', 'In Progress'),
            ('published', 'Published')
        )

class UserProfile(AbstractUser):
    pass


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default='')
    word_count = models.IntegerField(blank=True, default=0)
    twitter_post = models.TextField(blank=True, default='')
    status = models.CharField(
        max_length=10,
        choices=ARTICLE_STATUS,
        default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*>", "", self.content).replace("&nbsp;", "")
        self.word_count = len(re.findall(r"\b\w+\b", text))
        super().save(*args, **kwargs)
