# Generated by Django 5.0.6 on 2024-06-10 21:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_post_inquiry_alter_post_is_attending_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='scrap',
            field=models.ManyToManyField(blank=True, null=True, related_name='scraped', to=settings.AUTH_USER_MODEL),
        ),
    ]
