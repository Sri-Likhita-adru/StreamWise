# Generated by Django 3.2.6 on 2023-07-28 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_uploadedimage_stage2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimage',
            name='Stage2',
        ),
    ]
