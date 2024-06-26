# Generated by Django 5.0.6 on 2024-06-10 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_post_scrap_count_remove_post_scrap_post_scrap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='inquiry',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_attending',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_income_bracket',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='recruitment',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='wage',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
