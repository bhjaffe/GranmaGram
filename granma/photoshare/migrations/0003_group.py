# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0002_grouproleuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=35)),
                ('gru', models.ForeignKey(to='photoshare.GroupRoleUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
