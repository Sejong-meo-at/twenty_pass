from django.db import models

from django.utils import timezone
import random
# Create your models here.
class TwentyPass(models.Model):
    title = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.CharField(max_length=100)
    update_date = models.DateTimeField()

    def update_dates(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s"%self.title
