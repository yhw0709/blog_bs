from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Articles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'articles'
        ordering = ('-publish',)

    def __str__(self):
        return self.title
