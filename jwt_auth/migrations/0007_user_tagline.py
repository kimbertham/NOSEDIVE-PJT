# Generated by Django 3.0.7 on 2020-06-07 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0006_auto_20200604_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tagline',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
