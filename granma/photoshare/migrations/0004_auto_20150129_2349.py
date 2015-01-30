# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0003_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picfile', models.FileField(upload_to=b'photos/%Y/%m/%d')),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('creator', models.ForeignKey(to='photoshare.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gru',
            field=models.ForeignKey(to='photoshare.GroupRoleUser', null=True),
            preserve_default=True,
        ),
    ]
