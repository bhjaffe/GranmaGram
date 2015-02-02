# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0002_auto_20150201_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouproleuser',
            name='role',
            field=models.CharField(default=b'MBR', max_length=3, choices=[(b'VWR', b'Viewer'), (b'ADM', b'Admin'), (b'MBR', b'Member')]),
            preserve_default=True,
        ),
    ]
