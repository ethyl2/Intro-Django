# Generated by Django 3.0.5 on 2020-04-24 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
