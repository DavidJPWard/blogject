# Generated by Django 3.2.15 on 2022-09-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_featured_image_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_bio',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_since',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
