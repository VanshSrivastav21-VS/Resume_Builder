# Generated by Django 5.0.4 on 2024-04-23 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumebuilder', '0005_resume_delete_achievement_delete_education_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='state',
        ),
    ]