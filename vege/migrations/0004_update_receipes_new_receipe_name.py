# Generated by Django 5.0.2 on 2024-02-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_update_receipes'),
    ]

    operations = [
        migrations.AddField(
            model_name='update_receipes',
            name='new_receipe_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
