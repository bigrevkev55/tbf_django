# Generated by Django 3.1.6 on 2021-02-17 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boxers', '0005_remove_boxer_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxer',
            name='date_created',
        ),
    ]
