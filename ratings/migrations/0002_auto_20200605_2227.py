# Generated by Django 3.0.7 on 2020-06-05 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
