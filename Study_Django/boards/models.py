from django.db import models
from common.models import CommonModel # 빨간줄 무시


# Create your models here.
class Board(CommonModel):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=True)
    writer = models.CharField(max_length=20)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)

    ordering = ['-created_at']

    def __str__(self):
        return self.title

