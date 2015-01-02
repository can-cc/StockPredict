# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('predictCenter', '0004_auto_20141227_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstock',
            name='owner',
        ),
        migrations.AlterField(
            model_name='userstock',
            name='userId',
            field=models.ForeignKey(related_name='Id', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
