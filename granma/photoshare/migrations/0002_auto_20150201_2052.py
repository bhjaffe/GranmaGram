# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='creator',
            field=models.ForeignKey(to='photoshare.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='picfile',
            field=models.FileField(upload_to=b'photos/%Y/%m'),
            preserve_default=True,
        ),
    ]
