from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')
