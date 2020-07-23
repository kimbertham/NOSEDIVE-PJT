# Generated by Django 3.0.7 on 2020-07-18 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0005_forum_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('comment_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
