# Generated by Django 2.0.7 on 2018-07-15 12:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('measurements', '0003_rename_pings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instancerun',
            name='callback_auth_code',
        ),
    ]
