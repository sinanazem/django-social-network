# Generated by Django 5.0.1 on 2024-01-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]