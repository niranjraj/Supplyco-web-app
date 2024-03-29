# Generated by Django 3.1.3 on 2020-11-30 03:48

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20201130_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, default='media/avatars', upload_to=store.models.upload_image_path),
        ),
    ]
