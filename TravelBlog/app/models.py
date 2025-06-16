from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date = models.DateField()
    author = models.CharField(max_length=255)
    
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="auto"/>')
        return "No image"

    image_tag.short_description = 'Preview'


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.text[:30]}"
