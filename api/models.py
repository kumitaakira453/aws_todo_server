from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)  # detailが空でもOK
    deadLine = models.DateField(
        default=timezone.now
    )  # deadLineが指定されなければ今日の日付
    is_done = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
