from turtle import title
from unicodedata import category
from django.db import models
from django.utils import timezone
import os, uuid

def user_directory_path(instance, filename):
    if "." in filename:
        filename = filename.split('.')[0]
    return os.path.join('images/', filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Images(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    name =models.CharField(max_length=100)
    #file = models.FileField(upload_to=user_directory_path, default='images/default.jpg')
    image = models.ImageField(
        upload_to=user_directory_path, default='images/default.jpg')
    created = models.DateTimeField(default=timezone.now)