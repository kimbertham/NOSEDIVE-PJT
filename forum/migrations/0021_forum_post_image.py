# Generated by Django 3.0.7 on 2020-10-09 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0020_forumcomments_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='post_image',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
