# Generated by Django 3.0.7 on 2020-07-21 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0013_auto_20200721_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
