# Generated by Django 2.0.7 on 2018-07-12 12:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('instances', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zaphod',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('name', models.CharField(
                    max_length=100,
                    unique=True,
                    verbose_name='name')),
                ('hostname', models.CharField(
                    max_length=127,
                    unique=True,
                    validators=[django.core.validators.RegexValidator(
                        '([a-z¡-\uffff0-9](?:[a-z¡-\uffff0-9-]{0,61}[a-z¡-\uffff0-9])?'
                        '(?:\\.(?!-)[a-z¡-\uffff0-9-]{1,63}(?<!-))*'
                        '\\.(?!-)(?:[a-z¡-\uffff-]{2,63}|xn--[a-z0-9]{1,59})(?<!-)'
                        '\\.?|localhost)', message='Please provide a valid host name')],
                    verbose_name='hostname')),
                ('token', models.CharField(
                    max_length=40,
                    verbose_name='token')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]