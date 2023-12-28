from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('Política', 'Política'),
        ('Tecnología', 'Tecnología'),
        ('Ciencia', 'Ciencia'),
        ('Humor', 'Humor'),
    ]
        
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = RichTextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Humor')