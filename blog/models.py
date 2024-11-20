from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='articles/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_photo(self):
        try:
            return self.photo.url
        except:
            return "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"


class Comment(models.Model):
    title = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

