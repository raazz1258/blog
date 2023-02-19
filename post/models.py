from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField( auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
