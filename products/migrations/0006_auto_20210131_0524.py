# Generated by Django 3.1.3 on 2021-01-31 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_shippingaddress_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
