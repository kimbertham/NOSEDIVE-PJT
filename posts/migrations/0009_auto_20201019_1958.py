# Generated by Django 3.0.7 on 2020-10-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_profile_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
