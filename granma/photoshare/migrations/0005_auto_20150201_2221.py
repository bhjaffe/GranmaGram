# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0004_auto_20150201_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='gru',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gru',
        ),
        migrations.AddField(
            model_name='grouproleuser',
            name='group',
            field=models.ForeignKey(to='photoshare.Group', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grouproleuser',
            name='user',
            field=models.ForeignKey(to='photoshare.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
