# Generated by Django 5.0.1 on 2024-01-20 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_post_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
