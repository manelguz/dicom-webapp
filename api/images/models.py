from turtle import title
from unicodedata import category
from django.db import models
from django.utils import timezone
import os, uuid

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/', filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Images(models.Model):

    options = (
        ('active','Active'),
        ('deactivated', 'Deactivated'),
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title =models.CharField(max_length=100)
    image = models.ImageField(
        upload_to=user_directory_path, default='posts/default.jpg')
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=11, choices=options, default='active')
