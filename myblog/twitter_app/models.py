from django.db import models

# Create your models here.
class trends(models.Model):
    trend_text = models.CharField(max_length=128)

    def __str__(self):
        return self.trend_text


class tweets(models.Model):
    trends_topic = models.ForeignKey(trends , on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    writer = models.CharField(max_length = 128)

    def __str__(self):
        return self.content