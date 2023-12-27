from django.db import models

from polar_bear.models import Article

class Comment(models.Model):
    author = models.CharField(null=False, max_length=42, default="Anonyme")
    content = models.TextField(null=True, blank=True)
    date = models.DateField(null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.content