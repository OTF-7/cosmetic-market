# Generated by Django 4.0.1 on 2022-01-31 23:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('makeup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]