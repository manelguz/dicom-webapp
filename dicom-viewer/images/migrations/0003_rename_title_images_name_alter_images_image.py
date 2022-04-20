# Generated by Django 4.0.4 on 2022-04-12 23:29

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_remove_images_slug_remove_images_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to=images.models.user_directory_path),
        ),
    ]
