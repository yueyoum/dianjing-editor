# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientConfig',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'client_config',
            },
        ),
    ]
