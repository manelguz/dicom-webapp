from django.contrib import admin

# Register your models here.
from .models import Category, Images

admin.site.register(Category)
admin.site.register(Images)