# Generated by Django 5.0.4 on 2024-04-25 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumebuilder', '0013_remove_resumetemplate_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumetemplate',
            name='name',
        ),
    ]