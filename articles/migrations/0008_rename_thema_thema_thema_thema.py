# Generated by Django 3.2.9 on 2021-12-19 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20211219_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thema',
            old_name='thema_thema',
            new_name='thema',
        ),
    ]