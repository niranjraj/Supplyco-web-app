# Generated by Django 3.1.3 on 2021-04-08 16:24

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_help'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/10.png', upload_to=store.models.upload_image_path),
        ),
    ]