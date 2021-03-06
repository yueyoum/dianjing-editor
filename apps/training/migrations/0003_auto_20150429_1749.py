# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20150428_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='reward_type',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe7\xbb\x8f\xe9\xaa\x8c'), (2, b'\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'), (3, b'\xe7\x8a\xb6\xe6\x80\x81'), (10, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe9\x9a\x8f\xe6\x9c\xba'), (11, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe8\xbf\x9b\xe6\x94\xbb'), (12, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe7\x89\xb5\xe5\x88\xb6'), (13, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe5\xbf\x83\xe6\x80\x81'), (14, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe6\x9a\xb4\xe5\x85\xb5'), (15, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe9\x98\xb2\xe5\xae\x88'), (16, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe8\xbf\x90\xe8\x90\xa5'), (17, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe6\x84\x8f\xe8\xaf\x86'), (18, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe6\x93\x8d\xe4\xbd\x9c')]),
        ),
    ]
