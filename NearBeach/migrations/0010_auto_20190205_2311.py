# Generated by Django 2.1.5 on 2019-02-05 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0009_auto_20190205_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
