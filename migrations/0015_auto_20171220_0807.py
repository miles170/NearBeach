# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0014_auto_20171219_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products_and_services',
            name='product_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
