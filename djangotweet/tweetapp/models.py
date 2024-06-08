from django.db import models

# Create your models here.

class Tweet(models.Model):
    nickname = models.CharField(max_length=40)
    message = models.CharField(max_length=150)

    def __str__(self):
        return f"Tweet Nick: {self.nickname} Tweet: {self.message}"