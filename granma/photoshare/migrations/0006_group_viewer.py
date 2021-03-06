# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photoshare', '0005_auto_20150201_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='viewer',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
