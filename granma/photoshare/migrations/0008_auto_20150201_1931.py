# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0007_auto_20150201_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='gru',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='creator',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
