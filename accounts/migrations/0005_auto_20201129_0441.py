# Generated by Django 3.1.3 on 2020-11-29 04:41

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201129_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='aadhaar',
            field=models.CharField(max_length=12, unique=True, validators=[accounts.validators.validate_aadhaar]),
        ),
    ]
