# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0003_auto_20150201_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gru',
            field=models.ForeignKey(blank=True, to='photoshare.GroupRoleUser', null=True),
            preserve_default=True,
        ),
    ]
