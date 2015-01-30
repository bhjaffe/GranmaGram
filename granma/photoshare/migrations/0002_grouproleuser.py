# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupRoleUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(default=b'MBR', max_length=2, choices=[(b'VWR', b'Viewer'), (b'ADM', b'Admin'), (b'MBR', b'Member')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
