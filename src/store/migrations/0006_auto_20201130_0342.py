# Generated by Django 3.1.3 on 2020-11-30 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201129_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, default='', upload_to='avatar<function upload_image_path at 0x7fc208c349d0>'),
        ),
    ]
