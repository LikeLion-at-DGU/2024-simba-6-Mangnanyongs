# Generated by Django 5.0.6 on 2024-06-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_post_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
