# Generated by Django 4.2.1 on 2023-11-09 03:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likeapp', '0002_blog_like_user_blog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='bookmark_user',
            field=models.ManyToManyField(blank=True, related_name='bookmark_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
