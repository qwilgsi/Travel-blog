from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField(max_length=5000)
    date = models.DateField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title