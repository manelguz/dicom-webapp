from django.db import models
from django.utils import timezone
import os

def user_directory_path(instance, filename):
    if "." in filename:
        filename = filename.split('.')[0]
    return os.path.join('images/', filename + '.jpg')

def user_directory_path2(instance, filename):
    if "." in filename:
        filename = filename.split('.')[0]
    return os.path.join('images/', filename + '.dcm' )

class Images(models.Model):

    name =models.CharField(max_length=100)
    file_dicom = models.FileField(upload_to=user_directory_path2, default='images/default.dcm')
    image = models.ImageField(
        upload_to=user_directory_path, default='images/default.jpg')
    created = models.DateTimeField(default=timezone.now)