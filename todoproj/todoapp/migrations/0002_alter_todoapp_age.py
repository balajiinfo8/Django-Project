# Generated by Django 5.2.4 on 2025-07-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoapp',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
