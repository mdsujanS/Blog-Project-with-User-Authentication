# Generated by Django 5.1.4 on 2025-01-02 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_alter_profile_author'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
