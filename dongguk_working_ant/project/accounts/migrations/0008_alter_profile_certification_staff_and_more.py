# Generated by Django 5.0.6 on 2024-06-22 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_certification_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='certification_staff',
            field=models.FileField(blank=True, upload_to='staff_certification/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='certification_student',
            field=models.FileField(blank=True, upload_to='student_certification/'),
        ),
    ]
