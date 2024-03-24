from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
import math


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def calculate_reading_time(self):
        words_per_minute = 200  # Adjust according to your preference
        word_count = len(self.text.split())
        minutes = math.ceil(word_count / words_per_minute)
        return minutes
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title